import time
import json
import os
from sys import exit
def menu():
 file = open("settings.json", "r")
 data = json.load(file)
 file.close()
 print('================================')
 print(f'| [0] Exit And Save           |')
 print(f'| [1] Change All Settings     |')
 print(f'| [2] Change Token            |')
 print(f'| [3] Change Channel          |')
 print(f'| [4] Change Selfbot Commands |')
 print(f'| [5] Change Daily Mode       |')
 print(f'| [6] Change Stop Time        |')
 print(f'| [7] Change Interactions Mode|')
 print('================================')
 choice = input("Enter Your Choice: ")
 if choice == "0":
  raise SystemExit
 if choice == "1":
  t(data,"True")
  c(data,"True")
  oc(data,"True")
  daily(data,"True")
  stop(data,"True")
  interactions(data,"True")
 if choice == "2":
  t(data,"False")
 if choice == "3":
  c(data,"False")
 if choice == "4":
  oc(data,"False")
 if choice == "5":
  daily(data,"False")
 if choice == "6":
  stop(data,"False")
 if choice == "7":
  interactions(data,"False")
def t(data,all):
 data['token'] = input("Please Enter Your Account Token: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def c(data,all):
 data['channel'] = input("Please Enter Your Channel ID: ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def oc(data,all):
 data['prefix'] = input("Toggle Selfbot Commands, You Can Control Your Selfbot Using Commands (YES/NO): ")
 if data['prefix'].lower() == "yes":
  data['prefix'] = input("Enter Your Selfbot Prefix: ")
  data['allowedid'] = input("Do You Want Allow An User To Use Your Selfbot Commands? If Yes Enter The Account ID, Otherwise Enter \"None\": ")
  print("Great! You Can View Selfbot Commands At Option [3] Info At The Main Menu!")
  time.sleep(1)
 else:
  data['prefix'] = "NO"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def daily(data,all):
 data['daily'] = input("Toggle Automatically Claim Daily (YES/NO): ")
 if data['daily'].lower() == "no":
  data['daily'] = "None"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def stop(data,all):
 data['stop'] = input("Toggle Stop After A Specifice Time (YES/NO): ")
 if data['stop'].lower() == "yes":
  data['stop'] = input("Enter Stop Time (Seconds): ")
 else:
  data['stop'] = "NO"
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
def interactions(data,all):
 data['interactions'] = input("Toggle Use Interactions Command (Enter GuildID If Yes, Otherwise Enter \"NO\"): ")
 file = open("settings.json", "w")
 json.dump(data, file)
 file.close()
 print('Successfully saved!')
 if not all == "True":
  menu()
menu()
