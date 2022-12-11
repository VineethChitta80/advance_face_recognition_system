from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student

class Face_recognition_system:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #background image
        img =  Image.open("D:\wallpaper.jpg")
        img=img.resize((1530,790))
        self.photoimg=ImageTk.PhotoImage(img)

        #background setup
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=750)

        #title setup
        title_lbl=Label(f_lbl,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=20,width=1280,height=50)
        
        #Student button
        b1=Button(f_lbl,text="STUDENT",command=self.student_details,cursor="hand2",font=("times new roman",20,"bold"))
        b1.place(x=10,y=200,width=150,height=150)

        #face detection button
        b2=Button(f_lbl,cursor="hand2",text="FACE\nDETECTION",font=("times new roman",18,"bold"))
        b2.place(x=180,y=200,width=150,height=150)

        #Attendance button
        b3=Button(f_lbl,cursor="hand2",text="attendance",font=("times new roman",18,"bold"))
        b3.place(x=350,y=200,width=150,height=150)

        #chatbot button
        b4=Button(f_lbl,cursor="hand2",text="chatbot",font=("times new roman",20,"bold"))
        b4.place(x=1070,y=200,width=150,height=150)

        #train data button
        b5=Button(f_lbl,cursor="hand2",text="Train\ndata",font=("times new roman",20,"bold"))
        b5.place(x=10,y=370,width=150,height=150)

        #photos button
        b6=Button(f_lbl,cursor="hand2",text="Photos",font=("times new roman",20,"bold"))
        b6.place(x=180,y=370,width=150,height=150)

        #help desk button
        b7=Button(f_lbl,cursor="hand2",text="Help\ndesk",font=("times new roman",18,"bold"))
        b7.place(x=350,y=370,width=150,height=150)

        #exit button
        b8=Button(f_lbl,cursor="hand2",text="exit",font=("times new roman",20,"bold"))
        b8.place(x=1070,y=370,width=150,height=150)

    ####################Functions buttons####################

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()