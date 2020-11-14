import json
import hashlib
import os
from os import path
import time
import datetime
from email.message import EmailMessage
import imghdr
import smtplib

def check_username_password():
    username_input = input("Username: ")
    user_path = path.exists("~/Py/accountsystem/users/" + username_input + ".json")
    def check_password():
        password_input = input("Password: ")
        with open('~/Py/accountsystem/users/' + username_input + '.json') as f:
            check_password_full = json.load(f)
            check_password_str = check_password_full.get("password")
        input_password_encoded = hashlib.sha256(password_input.encode())
        input_password_hashed = input_password_encoded.hexdigest()
        if input_password_hashed == check_password_str:
            print("Correct Username and Password")
        else:
            time.sleep(0.4)
            print("Incorrect Password")
            time.sleep(0.3)
            print("Ending...")
            time.sleep(1)
            quit()
    if user_path == True:
        check_password()
    else:
        time.sleep(0.3)
        want_to_create_account = input("Username does not exist.\nDo you want to create an account [y/n]: ")
        time.sleep(0.2)
        def create_account():
            os.system("python3 ~/Py/accountsystem/createaccount.py")
        if want_to_create_account == "y":
            create_account()
        elif want_to_create_account == "yes":
            create_account()
        elif want_to_create_account == "Y":
            create_account()
        elif want_to_create_account == "Yes":
            create_account()
        else:
            time.sleep(0.3)
            print("Ending...")
            time.sleep(0.8)
            quit()

check_username_password()
