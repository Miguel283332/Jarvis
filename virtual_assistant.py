import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import ctypes
import pygame
import pyautogui
import math
import re
import random
import threading
from time import sleep
from os import system
system("cls")
# name of the virtual assistant
name = 'yarbiss'
import socket

def check_internet_connection():
    try:
        # Intenta conectarse a un servidor de Google
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if check_internet_connection():
    print("El dispositivo está conectado a Internet.")
else:
    print("Revisa tu conexión a internet!")
    exit()
# the flag help us to turn off the program
flag = 1

listener = sr.Recognizer()

engine = pyttsx3.init()

# get voices and set the first of them
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# editing default configuration
engine.setProperty('rate', 178)
engine.setProperty('volume', 0.9)
def talk(text):
    '''
        here, virtual assistant can talk
    '''
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
def open(application):
    talk(f"Abriendo {application}")
    pyautogui.hotkey("win", "r")
    pyautogui.typewrite(application)
    pyautogui.press("enter")

def listen():
    '''
        The program recover our voice and it sends to another function
    '''
    flag = 1
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            rec = rec.replace("garbi", name)
            if name in rec:
                rec = rec.replace(name, '')
                flag = run(rec)
            else:
                flag = run(rec)
    except:
        pass
    return flag

def run(rec):
    '''
        All the actions that virtual assistant can do
    '''
    print(f"Usuario: {rec}")
    rec = rec.replace("más", "+")
    rec = rec.replace("menos", "-")
    rec = rec.replace("entre", "/")
    rec = rec.replace("por", "*")
    rec = rec.replace("abrsm de", "abre cmd")
    rec = rec.replace("escribe r", "escribe dir")
    if 'algo' in rec:
        talk("Algo")
    if 'hola' in rec:
        talk("Buenos días")
    elif 'reproduce' in rec:
        if 'spotify' in rec:
            rec = rec.replace("spotify", "")
            rec = rec.replace("en", "")
            track_name = rec.replace('reproduce', "")
            pyautogui.press('win')
            sleep(0.2)
            pyautogui.typewrite('spotify', interval=0.2)
            pyautogui.press('enter')
            sleep(3.5)  
            # Enfocar la ventana de Spotify
            pyautogui.hotkey('alt', 'space')
            pyautogui.press('x')
            sleep(1)
            pyautogui.hotkey('ctrl', 'l')
            sleep(0.2)
            pyautogui.typewrite(track_name, interval=0.2)
            pyautogui.press('enter')
            sleep(2)
            pyautogui.moveTo("802", "392")
            pyautogui.click()
        else:
            music = rec.replace('reproduce', '')
            talk('Reproduciendo ' + music)
            pywhatkit.playonyt(music)
    elif rec.startswith("escribe"):
        rec = rec.replace("punto", ".")
        rec = rec.replace("coma", ",")
        rec = rec.replace("paréntesis", "(")
        rec = rec.replace("escribe", "")
        pyautogui.typewrite(rec)
    elif 'desliza' in rec:
        if 'abajo' in rec:
            pyautogui.scroll(-500)
        if 'arriba' in rec:
            pyautogui.scroll(500)
    elif 'volume' in rec:
        if 'sube' in rec:
            for i in range(10):
                pyautogui.press("volumeup")
        if 'baja' in rec:
            for i in range(10):
                pyautogui.press("volumedown")
    elif 'busca' in rec:
        if "wikipedia" in rec:
            rec = rec.replace('busca', "")
            rec = rec.replace("en", "")
            rec = rec.replace("la", "")
            order = rec.replace('busca', '')
            wikipedia.set_lang("es")
            info = wikipedia.summary(order, 1)
            talk(info)
        elif 'rae' in rec:
            rec = rec.replace('busca', "")
            rec = rec.replace("rae", "")
            rec = rec.replace("en", "")
            rec = rec.replace("la", "")
            talk("Buscando...")
            open(f"https://dle.rae.es/{rec}")
        else:
            talk("Buscando...")
            pyautogui.hotkey("win", "r")
            sleep(0.2)
            pyautogui.typewrite("chrome")
            sleep(0.1)
            pyautogui.press("enter")
            sleep(1)
            rec = rec.replace('busca', "")
            rec = rec.replace("cómo", "como")
            sleep(0.2)
            pyautogui.typewrite(rec)
            pyautogui.press("_")
            pyautogui.press("backspace")
            sleep(0.2)
            pyautogui.press("enter")
    elif any(op in rec for op in ['+', '-', '*', '/']):
        # Use regular expressions to extract the numbers and operator
        matches = re.findall(r'\d+', rec)
        if len(matches) == 2:
            num1 = int(matches[0])
            num2 = int(matches[1])
            if '+' in rec:
                result = num1 + num2
            elif '-' in rec:
                result = num1 - num2
            elif '*' in rec:
                result = num1 * num2
            elif '/' in rec:
                result = num1 / num2
                if result.is_integer():
                    pass
                else:
                   result = math.trunc(result* 100) / 100
            talk(f"El resultado es {result}")
        else:
            talk("No se encontraron dos números para realizar la operación.")
    elif 'minimiza' in rec:
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        ctypes.windll.user32.ShowWindow(hwnd, 6)
    elif 'estás' in rec:
        talk("Estoy a su completa disposición")
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'protocolo fiesta en casa' in rec:
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/migue/Escritorio/black.mp3")
        pygame.mixer.music.play()
    elif 'presiona'in rec:
        talk("Presionando...")
        if 'tecla' in rec:
            if "enter" in rec:
                pyautogui.press('enter')
            if "windows" in rec:
                pyautogui.press("win")
            if "control" in rec:
                rec = rec.replace("control", "")
                if "t" in rec:
                    pyautogui.hotkey("ctrl", "t")
                if "w" in rec:
                    pyautogui.hotkey("ctrl", "w") #no funciona bien la tecla ctrl + w
            else:
                print(rec)
        else: 
            pyautogui.click()
    elif 'abre' in rec:
        if 'chrome' in rec:
            open("chrome") 
        if 'spotify' in rec:
            open("spotify")
        if 'cmd' in rec:
            open("cmd")
    elif 'cierra' in rec:
        if 'app' or 'aplicación' or 'ventana' in rec:
            pyautogui.hotkey('alt', 'f4')
    elif 'apaga' in rec:
        if "ordenador" in rec:
            system("shutdown /s /f /t 0")
        else:
            flag = 0
            talk("Apagando sistemas...")
    else:
        talk("Vuelve a intentarlo, no reconozco: " + rec)
    return flag

while flag:
    flag = listen()