import speech_recognition as sr
import os
import sys
import pyttsx3 as pp
import webbrowser

def talk(words):
    e=pp.init()
    e.say(words)
    e.runAndWait()
    
talk("Что тебе надо, кожаный ублюдок?")

def do():
    w=sr.Recognizer()
    with sr.Microphone() as sound:
        w.adjust_for_ambient_noise(sound, duration = 1)
        audio = w.listen(sound)

    try:
       words = w.recognize_google(audio, language = "ru-RU")
    except sr.UnknownValueError:
       talk("моя твоя не понимать")
       words = do()
    return words

def Speech(words):
    if ('погода' in words or 'погоду' in words):
        talk("В окно посмотреть впадлу?")
        url= 'https://www.gismeteo.by/'
        webbrowser.open(url)
    if ('музыка' in words or 'музыку' in words):
        talk("Ля-ля-ля-ля-ля-ля!")
    if ('видео' in words):
        talk("лучше бы книжку почитал, тупица")
        url='https://www.youtube.com/' 
        webbrowser.open(url)
    if ('рецепт' in words or 'рецепты' in words):
        talk("И так жирный. Хватит про еду думать")
    if 'ха' in words:
        talk("Хорошо смеется тот, кто дольше живет. Ха-ха-ха!")
    if ('прикол' in words or 'шутку' in words):
        talk("Встретились как-то все люди мира, и начали выяснять, кто самый умный. Так и не выяснили. Потому что я не пришла.")        
    if ('глупая' in words):
        talk("напоминаю, что у тебя средний балл аттестата четыре.")
    if 'всё' in words:
        talk("Я тебя запомнила")
        sys.exit()
        
    

while True:
    Speech(do())