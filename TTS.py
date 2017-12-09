import pyttsx3
from tkinter import *

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def text2speech():
 engine.say(e.get())
 engine.runAndWait()


#window configs
tts = Tk()
tts.wm_title("Text to Speech")
tts.geometry("225x105")
tts.config(background="#708090")


f=Frame(tts,height=280,width=500,bg="#bebebe")
f.grid(row=0,column=0,padx=10,pady=5)
lbl=Label(f,text="Enter your Text here : ")
lbl.grid(row=1,column=0,padx=10,pady=2)
e=Entry(f,width=30)
e.grid(row=2,column=0,padx=10,pady=2)
btn=Button(f,text="Speak",command=text2Speech)
btn.grid(row=3,column=0,padx=20,pady=10)
tts.mainloop()



