import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import smtplib
import time
import json


scope = ['https://www.googleapis.com/auth/drive']


credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(credentials)


sheet = client.open('Enquiry').sheet1

email_list = pd.DataFrame(sheet.get_all_records())
all_names = email_list['Name']
all_emails = email_list['Email']
all_subjects = email_list['Subject']
all_messages = email_list['Message']

data = sheet.get_all_records()


with open('creds.json') as data_file:
    data = json.load(data_file)



your_name = data['your_name']
your_email = data['your_email']
your_password = data['your_password']

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)



sheet = client.open('Enquiry').sheet1

email_list = pd.DataFrame(sheet.get_all_records())

all_names = email_list['Name']
all_emails = email_list['Email']
all_subjects = email_list['Subject']
all_messages = email_list['Message']

length = len(all_emails)

while True:
    f = open('length.txt', "w")
    f.write(str(length))

    sheet = client.open('Enquiry').sheet1

    email_list = pd.DataFrame(sheet.get_all_records())

    all_names = email_list['Name']
    all_emails = email_list['Email']
    all_subjects = email_list['Subject']
    all_messages = email_list['Message']

    length2 = len(all_emails)
    
    if length == length2:
        print('No new messages')
    else:
        length = length2
        print(f"new message from {all_names[length-1]}")
        name = all_names[length-1]
        email = all_emails[length-1]
        subject = all_subjects[length-1]
        message = all_messages[length-1]

        full_email1 = (f"From: {your_name} <{your_email}>\n"
                    f"To: {your_name} <{your_email}>\n"
                    f"Subject: {subject} from {name}\n\n"
                    f"from: {email} \n\n {message}"
                    )
        sub = 'Thank you for messeging'
        mes = "This is just to confirm that the email is sent successfully. I will get in touch with you soon"
        full_email = (f"From: {your_name} <{your_email}>\n"
                    f"To: {name} <{email}>\n"
                    f"Subject: {sub}\n\n"
                    f"{mes}"
                    )
        try:
            server.sendmail(your_email, [email], full_email)
            server.sendmail(your_email, [your_email], full_email1)
            print(f'Email to {email} successfully sent!\n\n')
        except Exception as e:
            print('Email to {} could not be sent :( because {}\n\n'.format(email, str(e)))
    time.sleep(50)
server.close()
