# [GTT-Event-Bot]](https://telegram.me/)
### Current Version - 0.1
GTT-Event bot is a elegram bot which designed to gather details of various events occuring across the world. You can submit your event to the bot and it will automatically post it to the event channel on telegram and various other social media platforms

## How To Use

To use the bot you simply have to send below mentioned commands as text message.

/start - initial command to begin talking to the bot

/help - to get help, report bug and contribute

/submit - to submit your event

The sole purpose of this bot is to get following details from the organiser about the event.

* Event Type - #meetup
* Event Name - TechTalk Meetup #1
* Organised by - GlobalTechTalks
* Event Description - Virtual meetup on Cloud technologies
* Event day & date - Thursday, 01 January 1970
* Event time - 10am to 5pm
* Venue - HackerSpace Noida 
* RSVP or Registration Link  - https://meetup.com/GlobalTechTalks
* Contact Person - Mr Udit
* Email Id - contact@techtalk.co.in
* Phone No - 0123456789
* Keywords - #globaltechtalks #techtalk #meetup #event

## How To Deploy Your Instance Of This Bot

You need Python 3 and PIP installed for this to work
* Fork the repo to your profile
* `git clone link-to-repo.git` - Clone your copy of this repo to your local machine 
* `cd gtt-event-bot` - Move to the repo folder
* Install `pipenv` by running `pip install pipenv`
* Initialize the Python 3 environment by running `pipenv --three`
* `pipenv install -r requirements.txt` - install dependencies
* Create a new bot using [Botfather](https://telegram.me/botfather)
* Replace `Telegram-Bot-Token` with the token you get from Botfather in `config.txt` file
* Create a channel and make it public to get the username e.g. @mychannel
* We need unique ID of this channel, to get that first add your bot as administrator to the channel you just created
* Run `pipenv run python getid.py` and send `test` to the channel
* The channel ID will be printed onto the terminal
* Replace this unique ID with `Channel-Id` in `config.txt` file
* Now run `pipenv run python eventbot.py`
* You can now use commands mentioned above in `How To Use` section

## How To Contribute

* Create an issue in case you find one with the bot. Please mention how you got to that issue in brief.
* Fork this repo and create a feature/bug branch and make your changes to that.
* Create PR from feature/bug branch to master of this repo.