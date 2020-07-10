import pandas as pd
import xlrd
import smtplib

e = pd.read_excel("emails.xlsx")
emails = e['Email'].values

SENDEREMAIL = ""
PASSWORD = ""
subject = ""
message = ""


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDEREMAIL, PASSWORD)
body = "Subject: {}\n\n{}".format(subject, message)

for email in emails:
    server.sendmail(SENDEREMAIL, email, body)
    print("Email sent to " + email)
