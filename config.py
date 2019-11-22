#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.facebook import Facebook
import random

#insert your logincreds. PLEASE use your facebook email or it will fail 

user = ''
passwd = ''


#If you dont want to tag the Person -

tag = True

#Chose your favorit notificator
#if telegram True you can use it | else set it to False
#for telegram Setup Your Telegram Bot - to send you a message whom you wished happy birthday
telegram = True
bot_token = ''
bot_chatID = ''

#Chose how you want to run the programm
headless = True


"""4 Parts of wishing"""
#Chose your greedings
#GermanKRAUTversion
#opener
part1 = ["Hallo", "Hi!", "Hey!"] 
#wishes
part2 = ["Alles alles Gute!","Alles Gute zum Geburstag!","Alles Gute und viel Gesundheit!"]
#random saying
part3 = ["Ich wünsche einen schönen Tag und viel Spaß!","Und selbstverständlich einen wunderschönen Tag!"]
#byebye
part4 = ["Beste Grüße!", "Digitale Grüße"]

#if less them 4 parts delte them from the list
#randomizer mixxing wishes
greetings_mix = [part1, part2, part3, part4]
greeting = []
for part in greetings_mix:
    r = random.randint(0, len(part) - 1)
    greeting.append(part[r])
greetings = (" ".join(greeting))


#for whatsapp
#soon there will be a public whatsapp API we can use to send messages
# #whatsapp = True
#telnr = '0049123455667890'

#actuall programm

fb = Facebook(headless)
fb.login(user, passwd)
fb.security()
fb.persons()
fb.wishes(greetings, tag, user)
fb.telegram_bot_sendtext(bot_token, bot_chatID, telegram)
#fb.whatsapp_message(telnr)
fb.close()
