import smtplib
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MailAccount = 'jqly@outlook.com'
MailPassword = ''
SmtpUrl = 'smtp-mail.outlook.com'
SmtpPort = 587

MessageFormat = "Content-Type: text/plain;charset=utf-8\r\nSubject: %s\r\n\r\n%s"


def remind_me_please(subject: str, content: str, sendto='jqly@outlook.com'):
    account = MailAccount

    mail_content = MIMEMultipart('alternative')
    mail_content.set_charset('utf8')
    mail_content['Subject'] = subject
    mail_content.attach(MIMEText(content, 'plain'))

    try:
        server = smtplib.SMTP(SmtpUrl, port=SmtpPort)

        server.starttls()

        server.login(user=account, password=MailPassword)
        server.sendmail(from_addr=account, to_addrs=sendto, msg=mail_content.as_string())
        server.quit()
    except Exception as e:
        timestamp = datetime.now().strftime('%y-%m-%d, %H:%M')
        with open('reminder_log.txt', 'a+', encoding='utf8') as file:
            print('(%s) Error while sending mail\n%s' % (timestamp, e.args), file=file)


if __name__ == '__main__':
    message = 'I am Py!'
    remind_me_please(subject='About summer camp', content=message)
