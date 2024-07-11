from tkinter import *
from PIL import Image,ImageTk
import random

root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="blue")

#IMAGE

rock_img = ImageTk.PhotoImage(Image.open("userrock.png"))
paper_img = ImageTk.PhotoImage(Image.open("userpaper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("userscissor.png"))
rock_imgcom = ImageTk.PhotoImage(Image.open("comrock.png"))
paper_imgcom = ImageTk.PhotoImage(Image.open("compaper.png"))
scissor_imgcom = ImageTk.PhotoImage(Image.open("comscissor.png"))

user_label=Label(root,image=scissor_img,bg="blue")
com_label=Label(root,image=scissor_imgcom,bg="blue")
com_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#SCORE

userscore=Label(root,text=0,font=100,bg="blue",fg="white")
comscore=Label(root,text=0,font=100,bg="blue",fg="white")
comscore.grid(row=1,column=1)
userscore.grid(row=1,column=3)

#INDICATORS

u=Label(root,font=50,text="USER",bg="blue",fg="white")
com=Label(root,font=50,text="COMPUTER",bg="blue",fg="white")
u.grid(row=0,column=3)
com.grid(row=0,column=1)

#MSG 

msg=Label(root,font=50,bg="blue",fg="white")
msg.grid(row=3,column=2)

#update msg

def updatemsg(x):
    msg['text']=x

#updtae score

def updateuserscore():
    score=int(userscore["text"]) 
    score+=1
    userscore["text"]=str(score)

def  updatecomscore():
    score=int(comscore["text"])
    score+=1
    comscore["text"]=str(score)

#winner 
def checkwin(user,com):
    if user==com:
        updatemsg("Game Draw!")
        updateuserscore()
        updatecomscore()
        
    elif user=="rock":
        if com=="scissor":
            updatemsg("You win!")
            updateuserscore()
        else:
            updatemsg("You lose") 
            updatecomscore()   
    elif user=="paper":
        if com=="rock":
            updatemsg("You win!")
            updateuserscore()
        else:
            updatemsg("You lose!")
            updatecomscore()
    elif user=="scissor":
        if com=="paper":
            updatemsg("You win!")
            updateuserscore()
        else:
            updatemsg("You lose!")
            updatecomscore()

    else:
        pass
        


#update picture 
choice=["rock","paper","scissor"]
def updatepicture(x):
    #computer:
   
    Computer_choice=random.choice(choice)
    if Computer_choice =="rock":
        com_label.configure(image=rock_imgcom)
    elif Computer_choice=="paper":
        com_label.configure(image=paper_imgcom)
    else:
        com_label.configure(image=scissor_imgcom)


    #user :
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,Computer_choice)

#BUTTONS

rock=Button(root,width=20,height=2,text="ROCK",bg="#FAD02E",fg="white",command=lambda:updatepicture("rock"))
paper=Button(root,width=20,height=2,text="PAPER",bg="green",fg="white",command=lambda:updatepicture("paper"))
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="red",fg="white",command=lambda:updatepicture("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)
mainloop()