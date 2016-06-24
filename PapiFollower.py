import requests
import json
from MailSender import remind_me_please

PapiUrl = 'http://space.bilibili.com/ajax/member/getSubmitVideos?mid=1532165&pagesize=30&tid=0&keyword=&page=1'


def papi_follower():
    while True:
        try:
            r = requests.get(PapiUrl, timeout=5).text
            break
        except TimeoutError:
            continue
    video_list, video_cur_cnt = json.loads(r)['data']['vlist'], json.loads(r)['data']['count']

    with open('papi_videos.txt', 'r') as file:
        video_pre_cnt = json.load(fp=file)['count']
    if video_cur_cnt > video_pre_cnt:
        new_video_info = [v['title'] + ', ' + v['created'] for v in video_list[:video_cur_cnt - video_pre_cnt]]
        remind_me_please(subject='Papi updated!',
                         content='%d new papi!\n%s' % (video_cur_cnt - video_pre_cnt, '\n'.join(new_video_info)))
        with open('papi_videos.txt', 'w') as file:
            json.dump({'count':video_cur_cnt}, fp=file)

import time
if __name__ == '__main__':
    while True:
        papi_follower()
        time.sleep(30 * 60)
