#!/usr/bin/python
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate


# Mail Account
MAIL_ACCOUNT = '#####@gmail.com'
MAIL_PASSWORD = '#####'

# Sender Name
SENDER_NAME = u'zabbix@admin.io'

# Mail Server
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
# TLS
SMTP_TLS = True

def send_mail(recipient, subject, body, encoding='utf-8'):
    session = None
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = Header(SENDER_NAME, encoding)
    msg['To'] = recipient
    msg['Date'] = formatdate()
    try:
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        if SMTP_TLS:
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(MAIL_ACCOUNT, MAIL_PASSWORD)
        session.sendmail(MAIL_ACCOUNT, recipient, msg.as_string())
    except Exception as e:
        raise e
    finally:
        # close session
        if session:
            session.quit()

if __name__ == '__main__':
    '''
    recipient = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]
    '''
    if len(sys.argv) == 4:
        send_mail(
            recipient=sys.argv[1],
            subject=sys.argv[2],
            body=sys.argv[3])
    else:
        print ("requires 3 parameters (recipient, subject, body)")
