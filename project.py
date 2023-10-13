from gtts import gTTS
import os
import speech_recognition as sr
import datetime

def speak(audio):
    tts = gTTS(text=audio, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # You might need to install mpg321 to play the audio

