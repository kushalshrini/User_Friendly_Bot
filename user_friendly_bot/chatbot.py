import random
import Jokes as J
import read
import json
import pickle
import numpy as np
import pywhatkit
import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import Jokes as J
import webbrowser
import requests
import smtplib
from datetime import date
import nltk
# from cffi.setuptools_ext import execfile #for executing files
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
from flask import Blueprint,render_template,request
chatbot = Blueprint("chatbot", __name__, static_folder="static", template_folder="templates/search")

class driver:
    name=''
    phone=''

def op(q):
    webbrowser.open(q)

listener = sr.Recognizer()

# engine.setProperty('voice', voices[1].id)


def talk(text):
    engine = pyttsx3.init()
    if engine._inLoop:
        engine.endLoop()
    voices = engine.getProperty('voices')
    engine.say(text)
    engine.runAndWait()
    engine.startLoop(False)


lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot model.h5')



def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    result.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(intents_list, intents_json):
    global result
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


print("HELLO  I'm here USERFRIENDLY BOT")

def bot_response(user_input):
    command = user_input.lower()
    greetings=['hi','hello','yo']

    if command.lower() in greetings:
        return ('hello '+str(driver.name))

    if 'cal' in command:
        command=command.replace('cal','')
        res=eval(command)
        return ('The result is '+str(res))

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        return ('playing on youtube......')



    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        return (time)

    elif 'wiki' in command:
        person = command.replace('wiki', '')
        info = wikipedia.summary(person, sentences=2)
        talk(info)
        return (info)



    elif 'date' in command:
        # talk('sorry, I have a headache')
        today =date.today()
        talk(today)
        return (today)


    elif 'are you single' in command:
        relationship ='I am in a relationship with wifi'
        talk(relationship)
        return (relationship)

    elif 'joke' in command:
        JOKE = J.Jokes()
        #talk(JOKE)
        return (JOKE)



    elif 'distance between' in command:
        #API_KEY = 'AIzaSyBxTw8_FN3CMZs2wSsm3UScsyjrd1JM-E4'
        command=command.replace('distance between ','')
        command = command.replace('and','')
        # print(command)
        x=''
        y=''
        for i in command:
            if i != ' ':
                x+=i
            else:
                break
        print(x)
        command = command.replace(x , '')
        command = command.replace(' ', '')
        for i in command:
            if i != ' ':
                y+=i
            else:
                break
        print(y)
        # url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        # r = requests.get(url + 'origins = ' + x +
        #                 '&destinations = ' + y +
        #                 '&key = ' + api_key)
        #
        #
        # info = r.json()
        #
        # print(info)
        q = 'https://www.google.com/maps/dir/' + x + '/' + y + '/'
        op(q)
        return (talk('Opening on Google maps......'))

    elif 'distance from' in command:
        #api_key = 'AIzaSyBRJzS37T67xNTXxMWhDnuB_YWHqSTW8Nw'
        command=command.replace('distance from ', '')
        command = command.replace('to', '')
        # print(command)
        x=''
        y=''
        for i in command:
            if i != ' ':
                x+=i
            else:
                break
        print(x)
        command = command.replace(x , '')
        command = command.replace(' ', '')
        for i in command:
            if i != ' ':
                y+=i
            else:
                break
        print(y)
        # url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        # r = requests.get(url + 'origins = ' + x +
        #                 '&destinations = ' + y +
        #                 '&key = ' + api_key)
        #
        #
        # info = r.json()
        #
        # print(info)
        q = 'https://www.google.com/maps/dir/' + x + '/' + y + '/'
        op(q)
        return (talk('Opening on Google maps......'))

    elif 'route from' in command:
        #api_key = 'AIzaSyBRJzS37T67xNTXxMWhDnuB_YWHqSTW8Nw'
        command=command.replace('route from ', '')
        command = command.replace('to', '')
        # print(command)
        x=''
        y=''
        for i in command:
            if i != ' ':
                x+=i
            else:
                break
        print(x)
        command = command.replace(x , '')
        command = command.replace(' ', '')
        for i in command:
            if i != ' ':
                y+=i
            else:
                break
        print(y)
        # url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
        # r = requests.get(url + 'origins = ' + x +
        #                 '&destinations = ' + y +
        #                 '&key = ' + api_key)
        #
        #
        # info = r.json()
        #
        # print(info)
        q = 'https://www.google.com/maps/dir/' + x + '/' + y + '/'
        op(q)
        return (talk('Opening on Google maps......'))

    elif 'my location' in command:
        q = 'https://www.google.com/maps/search/my+location/'
        op(q)
        return (talk('Opening on Google maps......'))


    # elif 'exit' in command:
    #     break;

    else:

        ints = predict_class(command)
        res = get_response(ints, intents)
        return (res)
    

def write_to_file(name1, data):
    with open(name1, 'a') as f:
        f.write(data + "\n")

@chatbot.route("/")
def home():
    driver.name= request.args.get('name')
    driver.phone=request.args.get('phone')
    today = date.today()
    time = datetime.datetime.now().strftime('%I:%M %p')
    string=str(today)+'     '+str(time)+'       '+str(driver.name)+'       '+str(driver.phone)
    write_to_file('log.txt',string)
    return render_template("index.html")

@chatbot.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot_response(userText))
