import smtplib
from email.mime.text import MIMEText


class SendMail:

    def __init__(self):
        self.message = None
        self.sender = '@gmail.com'
        self.password = 'password'
        self.server = smtplib.SMTP("smtp.gmail.com", 587)

    def send_mail(self, message):
        self.server.starttls()

        try:
            self.server.login(self.sender, self.password)
            msg = MIMEText(message)
            msg['Subject'] = 'Test'
            self.server.sendmail(self.sender, 'recipient@mail.ru', msg.as_string())
            return "The message was sent successfully!"
        except Exception as _ex:
            return f"{_ex}\nCheck your login or password please"

    def email(self):
        message = input('ff: ')
        print(self.send_mail(message=message))


if __name__ == "__main__":
    SendMail().email()
