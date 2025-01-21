import smtplib
import pandas as pd


# including the subject file
with open("subject.txt", "r", encoding="utf-8") as file:
    subject = file.read()
# including the body file
with open("Body.txt", "r", encoding="utf-8") as file:
    body = file.read()
    
MY_email = input("Enter your email: ")
mails=pd.read_csv('Emails.csv')
Reciever_mails=mails['emails']

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(MY_email, "bndv cqoa vmsg czst")

for email in Reciever_mails:
    # print(email)
    server.sendmail(MY_email, email,"Subject: {}\n\n{}".format(subject, body))

server.quit()

    

