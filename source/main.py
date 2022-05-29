from colorama import init
init()
import os
from sys import *
import time
import requests
import atexit
from multiprocessing import Process, Pool
import random
import re
try:
 from inputimeout import inputimeout,TimeoutOccurred
except:
 from setup import install
 install()
 from inputimeout import inputimeout,TimeoutOccurred
import json
try:
  from discum import *
except:
  from setup import install
  install()
  from discum import *
print("""\
██████╗░░█████╗░███╗░░██╗██╗░░██╗  ░██████╗███████╗██╗░░░░░███████╗██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗████╗░██║██║░██╔╝  ██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║███████║██╔██╗██║█████═╝░  ╚█████╗░█████╗░░██║░░░░░█████╗░░██████╦╝██║░░██║░░░██║░░░
██║░░██║██╔══██║██║╚████║██╔═██╗░  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██╔══██╗██║░░██║░░░██║░░░
██████╔╝██║░░██║██║░╚███║██║░╚██╗  ██████╔╝███████╗███████╗██║░░░░░██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░
**Version: 1.0.0**""")
wbm=[36,45]
class client:
  commands=[
    "Pls hunt",
    "Pls fish",
    "Pls dig",
    "Pls beg"
    ]
  totalcmd = 0
  totaltext = 0
  stopped = False
  recentversion = "1.0.0"
  wait_time_daily = 60
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        daily = data["daily"]
        stop = data['stop']
        sm = data['sm']
        prefix = data['prefix']
        allowedid = data['allowedid']
        interactions = data['interactions']
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(2)
   from newdata import menu
   menu()
   os.execl(executable, executable, *argv)
  head = {'Authorization': str(token)}
  response = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
  if response.status_code == 200:
    pass
  elif response.status_code == 429:
    print(f"{color.fail}[ERROR]{color.reset} Too Many Requests! Try Again Later.")
    time.sleep(2)
    raise SystemExit
  elif response.status_code == 404:
    print(f"{color.fail}[ERROR]{color.reset} Invalid Token")
    time.sleep(2)
    raise SystemExit
  response = requests.get("https://api.github.com/repos/ahihiyou20/discord-selfbot-dankmemer-bot/releases/latest")
  if recentversion in response.json()["name"]:
    print(f"{color.warning}Checking Update... {color.reset}")
    time.sleep(0.5)
    print(f"{color.okgreen}No Update Available {color.reset}")
  else:
   print(f"{color.warning}Checking Update... {color.reset}")
   time.sleep(0.5)
   print(f"{color.warning}Update Available {color.reset}")
   print(f"{color.purple}Update Info:{color.reset}")
   time.sleep(0.5)
   print(response.json()["name"])
   print(response.json()["body"])
   choice = input(f"{color.warning}Do You Want To Update (YES/NO): {color.reset}")
   if choice.lower() == "yes":
    import update
   else:
    pass
  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Info              {color.reset}|')
  print('=========================')
try:
 print("Automatically Pick Option [1] In 10 Seconds.")
 choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
except TimeoutOccurred:
 choice = "1"
if choice == "1":
      pass
elif choice == "2":
 from newdata import menu
 menu()
elif choice == "3":
      print(f"{client.color.purple} =========Support========== {client.color.reset}")
      print(f"{client.color.purple}https://discord.gg/3kTrhbBVQm{client.color.reset}")
      print(" ")
      print(f"{client.color.purple} =========Disclaimer========={client.color.reset}")
      print(f"{client.color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
      print(" ")
      print(f'{client.color.purple} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      print(" ")
      print(f'{client.color.purple} =========Selfbot Commands=========={client.color.reset}')
      print("{Prefix}send {Message} [Send Your Provied Message}")
      print("{Prefix}restart [Restart The Selfbot]")
      print("{Prefix}exit [Stop The Selfbot]")
      print(" ")
      print("{Prefix} == Your Prefix")
      time.sleep(15)
      raise SystemExit
else:
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(1)
 os.execl(executable, executable, *argv)
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel and client.stopped != True:
    if m['author']['id'] == '270904126974590976' or m['author']['username'] == 'Dank Memer' or m['author']['discriminator'] == '5192' or m['author']['public_flags'] == 65536:
     if "don't have a fishing pole" in m['content'] and m['mentions'][0]['username'] == bot.gateway.session.user['username']:
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} You Don't Have A Fishing Pole! I'll Buy One For You!")
         bot.sendMessage(str(client.channel), "pls buy Fishing Pole")
         time.sleep(2)
     if "don't have a hunting rifle" in m['content'] and m['mentions'][0]['username'] == bot.gateway.session.user['username']:
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} You Don't Have A Hunting Rifle! I'll Buy One For You!")
         bot.sendMessage(str(client.channel), "pls buy Hunting Rifle")
         time.sleep(2)
     if "don't have a shovel" in m['content'] and m['mentions'][0]['username'] == bot.gateway.session.user['username']:
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} You Don't Have A Shovel! I'll Buy One For You!")
         bot.sendMessage(str(client.channel), "pls buy Shovel")
         time.sleep(2)
     if m['content'] == "" and m['embeds'][0]['type'] == "rich" and "title" in m['embeds'][0] and "banned" in m['embeds'][0]['title'] and m['mentions'][0]['username'] == bot.gateway.session.user['username']:
         print(f"{at()}{client.color.fail} [BANNED] {client.color.reset} Pain Bro You Got Banned!")
         time.sleep(2)
         bot.gateway.close()
def runner():
        global wbm
        command=random.choice(client.commands)
        command2=random.choice(client.commands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        client.totalcmd += 1
        if not command2==command and client.stopped != True:
          bot.typingAction(str(client.channel))
          time.sleep(13)
          bot.sendMessage(str(client.channel), command2)
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
          client.totalcmd += 1
        time.sleep(random.randint(wbm[0],wbm[1]))
def claim_daily():
 if client.daily.lower() == "yes" and client.stopped != True:
    bot.typingAction(str(client.channel))
    time.sleep(3)
    bot.sendMessage(str(client.channel), "Pls daily")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} Pls daily")
    client.totalcmd += 1
    time.sleep(3)
    msgs=bot.getMessages(str(client.channel), num=5)
    msgs=json.loads(msgs.text)
    daily = ""
    length = len(msgs)
    i = 0
    while i < length:
     if msgs[i]['author']['id']=='270904126974590976' and msgs[i]['content'] == "" and msgs[i]['embeds'] != [] and "daily" in msgs[i]['embeds'][0]['title']:
        daily = msgs[i]['embeds'][0]['description']
        i = length
     else:
        i += 1
    if not daily:
       time.sleep(5)
       client.totalcmd -= 1
       claim_daily()
    else:
       if "Your next daily" in daily:
         daily = re.findall('[0-9]+', daily)
         try:
          client.wait_time_daily = str(int(daily[0]) * 3600 + int(daily[1]) * 60 + int(daily[2]))
         except IndexError:
          client.wait_time_daily = str(int(daily[0]) * 3600 + int(daily[1]))
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Next Daily: {client.wait_time_daily}s")
       if "was placed" in daily:
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Claimed Daily")
def click_button(channelID, token, guildID, messageID, click):
   def getcustomID():
         buttons = {}
         headers = {
            'authorization' : token
         }
         r = requests.get(f'https://discord.com/api/v10/channels/{channelID}/messages?limit=5' , headers=headers)
         jsondat = json.loads(r.text)
         for message in jsondat:
          if message['id'] == messageID:
            for components in message['components']:
                for component in components['components']:
                    if 'label' in component:
                        buttons[ component['label'] ] = component['custom_id'].strip()
         return buttons
   buttons = getcustomID()
   def clickButton():
         headers = {
          'authorization' : token
                   }
         data = {
                    "type": 3,
                    "session_id": ' ',
                    "guild_id": guildID,
                    "channel_id": channelID,
                    "message_id": messageID,
                    "message_flags": 0,
                    "application_id": "270904126974590976",
                    "data": {
                        "component_type": 2,
                        "custom_id": buttons[random.choice(list(buttons.keys()))] if click == "random" else click
                            }
                }
         print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Clicked Button \"{list(buttons.keys())[list(buttons.values()).index(data['data']['custom_id'])]}\"")
         r = requests.post("https://discord.com/api/v10/interactions", json = data, headers = headers)
   clickButton()
def interactions():
   if client.interactions.lower() != "no" and client.stopped != True:
    bot.typingAction(str(client.channel))
    time.sleep(3)
    def search():
     bot.sendMessage(str(client.channel), "Pls search")
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} Pls search")
     client.totalcmd += 1
     msgs=bot.getMessages(str(client.channel), num=5)
     msgs=json.loads(msgs.text)
     messageID = 0
     length = len(msgs)
     i = 0
     while i < length:
      if msgs[i]['author']['id']=='270904126974590976' and "Where do you want to search" in msgs[i]['content']:
         messageID = msgs[i]['id']
         i = length
      else:
        i += 1
     if not messageID:
        time.sleep(5)
        client.totalcmd -= 1
        search()
     else:
        click_button(client.channel, client.token, client.interactions, messageID, "random")
    def crime():
     bot.sendMessage(str(client.channel), "Pls crime")
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} Pls crime")
     client.totalcmd += 1
     msgs=bot.getMessages(str(client.channel), num=5)
     msgs=json.loads(msgs.text)
     messageID = 0
     length = len(msgs)
     i = 0
     while i < length:
      if msgs[i]['author']['id']=='270904126974590976' and "What crime do you want to commit?" in msgs[i]['content']:
         messageID = msgs[i]['id']
         i = length
      else:
         i += 1
     if not messageID:
        time.sleep(5)
        client.totalcmd -= 1
        crime()
     else:
        click_button(client.channel, client.token, client.interactions, messageID, "random")
    def trivia():
     bot.sendMessage(str(client.channel), "Pls trivia")
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} Pls trivia")
     client.totalcmd += 1
     msgs=bot.getMessages(str(client.channel), num=1)
     msgs=json.loads(msgs.text)
     messageID = 0
     if msgs[0]['author']['id']=='270904126974590976' and msgs[0]['content'] == "":
         messageID = msgs[0]['id']
     else:
         trivia()
     if not messageID:
        time.sleep(5)
        client.totalcmd -= 1
        trivia()
     else:
        click_button(client.channel, client.token, client.interactions, messageID, "random")
    def highlow():
     bot.sendMessage(str(client.channel), "Pls highlow")
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} Pls highlow")
     client.totalcmd += 1
     msgs=bot.getMessages(str(client.channel), num=1)
     msgs=json.loads(msgs.text)
     messageID = 0
     if msgs[0]['author']['id']=='270904126974590976' and msgs[0]['content'] == "":
         messageID = msgs[0]['id']
     else:
         highlow()
     if not messageID:
        time.sleep(5)
        client.totalcmd -= 1
        highlow()
     else:
        click_button(client.channel, client.token, client.interactions, messageID, "random")
    trivia()
    highlow()
    search()
    crime()
@bot.gateway.command
def othercommands(resp):
 prefix = client.prefix
 if resp.event.message:
   m = resp.parsed.auto()
   if m['author']['id'] == bot.gateway.session.user['id'] or m['channel_id'] == client.channel and m['author']['id'] == client.allowedid:
    if prefix == "None":
     bot.gateway.removeCommand(othercommands)
     return
    if "{}send".format(prefix) in m['content'].lower():
     message = m['content'][6::]
     bot.sendMessage(str(m['channel_id']), message)
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {message}")
    if "{}restart".format(prefix) in m['content'].lower():
     bot.sendMessage(str(m['channel_id']), "Restarting...")
     print(f"{client.color.okcyan} [INFO] Restarting...  {client.color.reset}")
     time.sleep(1)
     os.execl(executable, executable, *argv)
    if "{}exit".format(prefix) in m['content'].lower():
     bot.sendMessage(str(m['channel_id']), "Exiting...")
     print(f"{client.color.okcyan} [INFO] Exiting...  {client.color.reset}")
     bot.gateway.close()
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  daily_time = 0
  main=time.time()
  stop=main
  interactions_time=0
  while x:
    if client.stopped == True:
       break
    else:
      runner()
       if time.time() - main > random.randint(300, 600) and client.stopped != True:
        main=time.time()
        print(f"{at()}{client.color.okblue} [INFO]{client.color.reset} Sleeping To Avoid Ban")
        time.sleep(random.randint(120, 180))
      if time.time() - daily_time > int(client.wait_time_daily) and client.stopped != True:
        claim_daily()
        daily_time = time.time()
      if client.stop.lower() == "yes" and client.stopped != True:
       if time.time() - stop > int(client.stop):
         bot.gateway.close()
      if time.time() - interactions_time > random.randint(60, 100):
        interactions()
        interactions_time = time.time()
def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2= Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol=Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)
@atexit.register
def atexit():
 print(f"{client.color.okgreen}Total Number Of Commands Executed: {client.totalcmd}{client.color.reset}")
 time.sleep(0.5)
 print(f"{client.color.purple} [1] Restart {client.color.reset}")
 print(f"{client.color.purple} [2] Support {client.color.reset}")
 print(f"{client.color.purple} [3] Exit    {client.color.reset}")
 try:
  print("Automatically Pick Option [3] In 10 Seconds.")
  choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
 except TimeoutOccurred:
  choice = "3"
 if choice == "1":
  os.execl(executable, executable, *argv)
 elif choice == "2":
  print("Having Issue? Tell Us In Our Support Server")
  print(f"{client.color.purple} https://discord.gg/3kTrhbBVQm {client.color.reset}")
 elif choice == "3":
  bot.gateway.close()
 else:
  bot.gateway.close()
