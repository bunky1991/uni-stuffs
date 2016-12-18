from __future__ import print_statement
import random
from speech import *

CONVERSING = True

memory = []
greetings = ['hola', 'hello', 'hi', 'Hi', 'Hey!', 'hey']
questions = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
validations = ['yes','yeah','yea','no','No','Nah','nah']
verifications = ['Are you sure?','You sure?','you sure','sure',"Sure?"]

while CONVERSING:
    lang = 'en-US'
    speed = .3

    userInput = raw_input (">>>Me: ")
    if userInput in greetings:
        random_greeting = random.choice(greetings)
        say(random_greeting,lang,speed)
        print ("random_greeting")
        memory.append((userInput,random_greeting))
    elif userInput in question:
        random_response = random.choice(responses)
        say(random_response,lang,speed)
        memory.append((userInput,random_response))
        print ("random_response")
    else:
        say("Sorry i dont understand the question",lang,speed)
        CONVERSING = False

for conversations in memory:
    print ("conversatations")

