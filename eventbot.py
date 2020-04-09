from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction, ParseMode
from datetime import datetime, timedelta
from time import sleep
import logging
import requests
import re
import os
import json
import sys
import signal
import subprocess

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

"""
---Process ID Management Starts---
This part of the code helps out when you want to run your program in background using '&'. This will save the process id of the program going in background in a file named 'pid'. Now, when you run you program again, the last one will be terminated with the help of pid. If in case the no process exist with given process id, simply the `pid` file will be deleted and a new one with current pid will be created.
"""
currentPID = os.getpid()
if 'pid' not in os.listdir():
    with open('pid', mode='w') as f:
        print(str(currentPID), file=f)
else:
    with open('pid', mode='r') as f:
        try:
            os.kill(int(f.read()), signal.SIGTERM)
            print("Terminating previous instance of " +
                  os.path.realpath(__file__))
        except ProcessLookupError:
            subprocess.run(['rm', 'pid'])
    with open('pid', mode='w') as f:
        print(str(currentPID), file=f)
"""
---Process ID Management Ends---
"""

"""
---Token Management Starts---
This part will check for the config.txt file which holds the Telegram and Channel ID and will also give a user friendly message if they are invalid. New file is created if not present in the project directory.
"""
configError = "Please open config.txt file located in the project directory and replace the value '0' of Telegram-Bot-Token with the Token you recieved from botfather."
if 'config.txt' not in os.listdir():
    with open('config.txt', mode='w') as f:
        json.dump({'Telegram-Bot-Token': 0, 'Channel-Id': 0}, f)
        print(configError)
        sys.exit(0)
else:
    with open('config.txt', mode='r') as f:
        config = json.loads(f.read())
        if config["Telegram-Bot-Token"]:
            print("Token Present, continuing...")
            TelegramBotToken = config["Telegram-Bot-Token"]
            if config["Channel-Id"]:
                ChannelId = config["Channel-Id"]
            else:
                    print("Channel ID is not present in config.txt. Please follow instruction on README.md, run getid.py and replace the Channel ID you obtain.")
        else:
            print(configError)
            sys.exit(0)
"""
---Token Management Ends---
"""

updater=Updater(token=TelegramBotToken)
dispatcher=updater.dispatcher

EventDetails = {}

print("I'm On..!!")

def start(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        bot.sendMessage(chat_id=update.message.chat_id,text='''
Hi! Let's begin /submit
Use /help to get /help''')

def help(bot, update):
        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        bot.sendMessage(chat_id=update.message.chat_id,text='''
Only command you should be using is /submit
Event Type - #meetup
Event Name - TechTalk Meetup #1
Organised by - GlobalTechTalks
Event Description - Virtual meetup on Cloud technologies
Event day & date - Thursday, 01 January 1970
Event time - 10am to 5pm
Venue - HackerSpace Noida 
RSVP or Registration Link  - https://meetup.com/GlobalTechTalks
Contact Person - Mr Udit
Email Id - contact@techtalk.co.in
Phone No - 0123456789
Keywords - #globaltechtalks #techtalk #meetup #event

To report a bug or contribute to this bot visit https://techtalk.co.in
''')

def submitEvent(bot, update):
        global EventDetails

        bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
        EventDetails[update.message.chat_id] = []
        bot.sendMessage(chat_id=update.message.chat_id,text='''
After your submission your event will be posted on our channel''')
        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter Event  Name''')

def addDetails(bot, update):
        global EventDetails
        
        if update.message != None and update.message.chat_id in EventDetails.keys():
                if len(EventDetails[update.message.chat_id]) == 0:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter event type(#meetup #hackathon #webinar #onedayhackathon) ''')
                elif len(EventDetails[update.message.chat_id]) == 1:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter Event Description
(Share links related to Event detail here)''')
                elif len(EventDetails[update.message.chat_id]) == 2:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter Event Day and Date
(e.g Thursday, 01 January 1970) ''')
                elif len(EventDetails[update.message.chat_id]) == 3:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter Event Time
(e.g. 10am to 4pm)''')
                elif len(EventDetails[update.message.chat_id]) == 4:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter Event Venue Location
(Share the address or the google maps link here :)''')
                elif len(EventDetails[update.message.chat_id]) == 5:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter RSVP or Registration link
(e.g. Last week of August or specific calender date)''')
                elif len(EventDetails[update.message.chat_id]) == 6:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Keywords
(e.g. #python #azure #techtalks etc.)''')
                elif len(EventDetails[update.message.chat_id]) == 7:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Enter name of the contact person
(e.g. Mr. Kumar)''')
                elif len(EventDetails[update.message.chat_id]) == 8:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Organized by : 
(e.g. Name of the organisation/company/meetup group)''')

                elif len(EventDetails[update.message.chat_id]) == 9:
                        EventDetails[update.message.chat_id].append(update.message.text)
                        bot.sendMessage(chat_id=update.message.chat_id,text='''
Your Email ID
(e.g. some@thing.com)''')
                elif len(EventDetails[update.message.chat_id]) == 10:
                        if re.match(r"[^@]+@[^@]+\.[^@]+", update.message.text):
                                EventDetails[update.message.chat_id].append(update.message.text)
                                bot.sendMessage(chat_id=update.message.chat_id,text='''
Your 10 Digit Phone  No
(e.g. 0123456789)''')
                        else:
                                bot.sendMessage(chat_id=update.message.chat_id,text='''Enter valid email address''')
                elif len(EventDetails[update.message.chat_id]) == 11:
                        if re.match(r"^.{10,10}$", update.message.text):
                                EventDetails[update.message.chat_id].append(update.message.text) 
                                bot.sendMessage(parse_mode=ParseMode.MARKDOWN, chat_id=ChannelId, text='''
*Event Type* - ''' + EventDetails[update.message.chat_id][1] + '''
*Event Name* - ''' + EventDetails[update.message.chat_id][0] + '''
*Organised by* - ''' + EventDetails[update.message.chat_id][9] +'''
*Event Description* - ''' + EventDetails[update.message.chat_id][2] + '''
*Event day & date* - ''' + EventDetails[update.message.chat_id][3] + '''
*Event time* - ''' + EventDetails[update.message.chat_id][4] + '''
*Venue* - ''' + EventDetails[update.message.chat_id][5] + '''
*RSVP or Registration Link * - ''' + EventDetails[update.message.chat_id][6] + '''
*Contact Person* - ''' + EventDetails[update.message.chat_id][8] +'''
*Email Id* - ''' + EventDetails[update.message.chat_id][10] +'''
*Phone No* - ''' + EventDetails[update.message.chat_id][11] +'''
*Keywords* - ''' + EventDetails[update.message.chat_id][7])
                                bot.sendMessage(chat_id=update.message.chat_id,text='''Your Event has been posted to our channel''')
                        else:
                                bot.sendMessage(chat_id=update.message.chat_id,text='''Please enter valid phone number''')
        elif update.message.chat.type == 'private':
                bot.sendMessage(chat_id=update.message.chat_id,text='''Please use /submit to submit Events''')

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('submit', submitEvent))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.text, addDetails))

updater.start_polling()
