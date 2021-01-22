from gtts import gTTS
import os
f = open('abc.txt')
x = f.read()
audio = gTTS(text=x, lang='en', slow=False)
audio.save('abc.wav')
os.system('abc.wav')
