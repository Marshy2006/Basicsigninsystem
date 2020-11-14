import json
import hashlib
import os
from os import path
import time
import datetime
import subprocess
import re
from random import randint
from email.message import EmailMessage
import imghdr
import smtplib

date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def end():
    print("ending...")
    time.sleep(0.3)
    quit()

def want_to_sign_in():
    from signin import check_username_password
    def signin():
        check_username_password()
    sign_in = input("do you want to sign in? [y/n] ")
    if sign_in == "y":
        signin()
    elif sign_in == "yes":
        signin()
    elif sign_in == "Y":
        signin()
    elif sign_in == "Yes":
        signin()
    else:
        end()

def emailcheck():
    email_regex = "[^@]+@[^@]+\.[^@]+"
    email_input = input("Email: ")
    emailcheck.email_input = email_input
    if(re.search(email_regex,email_input)):
        emailcheck.email_valid = True
        print("email valid")
    else:
        print("invalid email")
        emailcheck.email_valid = False
while True:
    emailcheck()
    if emailcheck.email_valid == True:
        break
    elif emailcheck.email_valid == False:
        continue

def verify_email():
    verif_code = randint(100000,999999)
    RECIPIENT = emailcheck.email_input
    MESSAGE_SUBJECT = "Email Verification"
    MESSAGE_CONTENTS = "verification code: " + str(verif_code) + "\n\n" + date_time
    EMAIL_ADDRESS = 'do.not.reply.automatedmessages@gmail.com'
    EMAIL_PASSWORD = 'EMAILPASSWORD'
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        msg = EmailMessage()
        msg['Subject'] = MESSAGE_SUBJECT
        msg['From'] = EMAIL_ADDRESS
        msg.set_content(MESSAGE_CONTENTS)
        msg['To'] = RECIPIENT
        smtp.send_message(msg)
    print("Verificaation email has been sent")
    print("didn't get an email? type 'resend' in the next input")
    verif_input = input("Verification code: ")
    if str(verif_input) == str(verif_code):
        print("correct verification code")
        verify_email.email_verified = True
    elif verif_input == "resend" or "Resend":
        print("need to resend")

while True:
    verify_email()
    if verify_email.email_verified == True:
        break
    elif verify_email.email_verified == False:
        continue

print("continuing")
email_input = emailcheck.email_input

def check_username():
    username_input = input("Username: ")
    user_path = path.exists("~/Py/accountsystem/users/" + username_input + ".json")
    def new_account():
        password_input = input("Password: ")
        input_password_encoded = hashlib.sha256(password_input.encode())
        input_password_hashed = input_password_encoded.hexdigest()
        password_json_write = {"password": "" + input_password_hashed + "", "email": "" + email_input + ""}
        with open("~/Py/accountsystem/users/" + username_input + ".json", 'w') as f:
            json.dump(password_json_write, f)
        print("account created")
    if user_path == False:
        new_account()
        want_to_sign_in()
    elif user_path == True:
        print("account already exists")
        want_to_sign_in()

check_username()