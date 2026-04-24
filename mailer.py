import smtplib
from email.mime.text import MIMEText
import os

def send_mail(to_addr, subject, content):
    from_addr = "619488300@qq.com"
    password = os.environ.get("MAIL_PASS")
    mail_host = "smtp.qq.com"

    msg = MIMEText(content, "plain", "utf-8")
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP_SSL(mail_host, 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
