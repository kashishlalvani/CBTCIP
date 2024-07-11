import sounddevice 
from scipy.io.wavfile import write 
from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import time

root=Tk()
root.geometry("500x600")
root.resizable(False,False)
root.title("record voice")
root.config(bg="gray")

def file():
    dur=int(a.get())
    record=sounddevice.rec((dur*44100),samplerate=44100,channels=2)
    try:
        temp=int(a.get())
    except:
        print("please enter right value!")

    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1

        if temp==0:
            messagebox.showinfo("Time countdown","time's up")
        l1=Label(text=f"{str(temp)}",font="arial 40",width=4,bg="gray").place(x=190,y=500)
    sounddevice.wait()
    write("recording.wav",44100,record)
       

    
mikeimg=PhotoImage(file="mike.png")
l=Label(root,image=mikeimg)
root.iconphoto(FALSE,mikeimg)

    

img1=PhotoImage(file="mic.png")
imgl=Label(image=img1,bg="gray")
imgl.pack(padx=4,pady=4)

name=Label(text="Voice Recoder",font="arial 30 bold",bg="gray",fg="white")
name.pack()

    
a=StringVar()
sec=Entry(root,textvariable=a,font="arial 30",width=13)
sec.pack(padx=10)
msg=Label(text="Enter time in Seconds!",font="arial 15",background="gray",fg="white").pack()

record=Button(root,font="arial 20",text="Record",bg="black",fg="white",command=file)
record.pack(pady=30)
    




root.mainloop()

   
 






















