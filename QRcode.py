from tkinter import*
screen=Tk()
screen.title('QR code')
screen.maxsize(width=450,height=250)
screen.minsize(width=465,height=250)
screen.configure(bg='blue')

def on_leavegenerate(s):
    generate.configure(bg='pink')
def on_entergenerate(s):
    generate.configure(bg='orange')

def on_leaveclear(s):
    clean.configure(bg='pink')
def on_enterclear(s):
    clean.configure(bg='orange')

def on_leaveQuit(s):
        Quit.configure(bg='pink')
def on_enterQuit(s):
    Quit.configure(bg='orange')



###################################33
QR_ID_label=Label(screen,text='Enter Your ID',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_ID_label.place(x=20,y=40)

QR_Name_label=Label(screen,text='Enter Your Message ',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_Name_label.place(x=20,y=80)

QR_Message_label=Label(screen,text='Enter Your message',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_Message_label.place(x=20,y=120)

QR_notifaction_label=Label(text='notification :',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_notifaction_label.place(x=20,y=220)
notifaction_box=Label(screen,text='',font=('arial',13,'italic bold'),bg='pink',width=27)
notifaction_box.place(x=210,y=220)

###################################
ID_entery_box=Entry(screen,font=('arial',10,'italic bold'),bg='pink',bd=5,width=23)
ID_entery_box.place(x=280,y=40)

Name_entry_box=Entry(screen,font=('arial',10,'italic bold'),bg='pink',bd=5,width=23)
Name_entry_box.place(x=280,y=80)

Message_entery_box=Entry(screen,font=('arial',10,'italic bold'),bg='pink',bd=5,width=23)
Message_entery_box.place(x=280,y=120)




########################
generate=Button(screen,text='Generate',font=('arial',10,' bold'),bg='pink',bd=5,width=10,)
generate.place(x=30,y=170)


clean=Button(screen,text='clean',font=('arial',10,' bold'),bg='pink',bd=5,width=10,)
clean.place(x=190,y=170)


Quit=Button(screen,text='Quit',font=('arial',10,' bold'),bg='pink',bd=5,width=10,)
Quit.place(x=350,y=170)
#######################################
generate.bind('<Enter>',on_entergenerate)
generate.bind('<Leave>',on_leavegenerate)

clean.bind('<Enter>',on_enterclear)
clean.bind('<Leave>',on_leaveclear)

Quit.bind('<Enter>',on_enterQuit)
Quit.bind('<Leave>',on_leaveQuit)

































screen.mainloop()