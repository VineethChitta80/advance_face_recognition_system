from cProfile import label
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cx_Oracle

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition Attendance System")

        #variables
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_usn=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_gen=StringVar()

        #background setup
        f_lbl=Label(self.root,bg="black")
        f_lbl.place(x=0,y=0,width=1530,height=750)

        #title setup
        title_lbl=Label(f_lbl,text="Student Management System",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=20,width=1280,height=50)

        #frame setup
        main_frame=Frame(f_lbl,bd=5)
        main_frame.place(x=8,y=70,width=1250,height=550)
        
        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Course Details",font=("ariel",15,"bold"))
        left_frame.place(x=5,y=5,width=610,height=530)

        #current course in left label frame
        current_course=LabelFrame(left_frame,bd=2,relief=RIDGE,text="current course",font=("ariel",12,"bold","underline"))
        current_course.place(x=5,y=20,width=596,height=100)

        #department information in current course
        dept_lbl=Label(current_course,text="department : ",font=("ariel",12,"bold"))
        dept_lbl.grid(row=0,column=0,padx=5,pady=5)

        dept_select=ttk.Combobox(current_course,textvariable=self.var_dep,font=("ariel",12),state="readonly")
        dept_select["values"]=("cse","ise","mechanical","civil","eee","ece")
        dept_select.grid(row=0,column=1,padx=5,pady=5)

        #semester information in current course
        sem_lbl=Label(current_course,text="semester : ",font=("ariel",12,"bold"))
        sem_lbl.grid(row=1,column=0,padx=5,pady=5)

        sem_select=ttk.Combobox(current_course,textvariable=self.var_sem,font=("ariel",12),state="readonly")
        sem_select["values"]=("1","2","3","4","5","6","7","8")
        sem_select.grid(row=1,column=1,padx=5,pady=5)

        #class student information in left label frame
        student_info=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student information",font=("ariel",12,"bold","underline"))
        student_info.place(x=5,y=130,width=596,height=350)
       
        #usn label
        usn_lbl=Label(student_info,text="USN : ",font=("ariel",12,"bold"))
        usn_lbl.grid(row=0,column=0,padx=5,pady=5)
        
        #usn entry field
        usn_entry=ttk.Entry(student_info,textvariable=self.var_usn,width=20,font=("ariel",12,"bold"))
        usn_entry.grid(row=0,column=1,padx=5,pady=5)

        #name label
        student_name_lbl=Label(student_info,text="Name : ",font=("ariel",12,"bold"))
        student_name_lbl.grid(row=1,column=0,padx=5,pady=5)

        #student name entry field
        student_name_entry=ttk.Entry(student_info,textvariable=self.var_name,width=20,font=("ariel",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5)

        #division label
        division_lbl=Label(student_info,text="Division : ",font=("ariel",12,"bold"))
        division_lbl.grid(row=2,column=0,padx=5,pady=5)

        #division entry field
        division_select=ttk.Combobox(student_info,textvariable=self.var_div,font=("ariel",12),state="readonly")
        division_select["values"]=("A","B")
        division_select.grid(row=2,column=1,padx=5,pady=5)

        #email label
        email_lbl=Label(student_info,text="Mail ID : ",font=("ariel",12,"bold"))
        email_lbl.grid(row=3,column=0,padx=5,pady=5)

        #email entry field
        email_entry=ttk.Entry(student_info,textvariable=self.var_email,width=20,font=("ariel",12,"bold"))
        email_entry.grid(row=3,column=1,padx=5,pady=5)

        #phone number label
        phone_lbl=Label(student_info,text="Phone number : ",font=("ariel",12,"bold"))
        phone_lbl.grid(row=4,column=0,padx=5,pady=5)

        #phone number entry field
        phone_entry=ttk.Entry(student_info,textvariable=self.var_phone,width=20,font=("ariel",12,"bold"))
        phone_entry.grid(row=4,column=1,padx=5,pady=5)

        #gender label
        gender_lbl=Label(student_info,text="Gender : ",font=("ariel",12,"bold"))
        gender_lbl.grid(row=5,column=0,padx=5,pady=5)

        #gender entry field
        division_select=ttk.Combobox(student_info,textvariable=self.var_gen,font=("ariel",12),state="readonly")
        division_select["values"]=("Male","Female","Others")
        division_select.grid(row=5,column=1,padx=5,pady=5)

        #take photo sample buttomn
        photo_btn=Button(student_info,text="Take Photo sample",font=("ariel",12,"bold"),bg="black",fg="white")
        photo_btn.grid(row=6,column=1,padx=5,pady=5)

        #save button
        save_btn=Button(student_info,text="Save",command=self.add_data,font=("ariel",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=7,column=1,padx=5,pady=5)

        #########################
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="student database info",font=("ariel",15,"bold"))
        right_frame.place(x=620,y=5,width=610,height=530)

        #search frame
        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search system",font=("ariel",15,"bold"))
        search_frame.place(x=5,y=10,width=550,height=150)

        #search field
        search_lbl=Label(search_frame,text="USN : ",font=("ariel",12,"bold"))
        search_lbl.grid(row=0,column=0,padx=5,pady=5)

        #search by usn entry field
        search_entry=ttk.Entry(search_frame,width=20,font=("ariel",12,"bold"))
        search_entry.grid(row=0,column=1,padx=5,pady=5)

        #search button
        search_btn=Button(search_frame,text="Search",font=("ariel",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=1,column=1,padx=5,pady=5)

        #info frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="student info",font=("ariel",15,"bold"))
        table_frame.place(x=5,y=180,width=550,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dept","sem","USN","name","Division","email","phone","gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.student_table.heading("dept",text="Department")
        self.student_table.heading("sem",text="semester")
        self.student_table.heading("USN",text="USN")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("gender",text="Gender")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)

    ################## data manipulation functions ###############
    def add_data(self):
        if self.var_dep.get()=="" or self.var_name.get()=="" or self.var_usn=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=cx_Oracle.connect('project/a@localhost:1521/orcl')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(:dep,:sem,:usn,:name,:div,:email,:phone,:gen)",{"dep":self.var_dep.get(),"sem":self.var_sem.get(),"usn":self.var_usn.get(),"name":self.var_name.get(),"div":self.var_div.get(),"email":self.var_email.get(),"phone":self.var_phone.get(),"gen":self.var_gen.get()})
                conn.commit()
                conn.close
                messagebox.showinfo("success","details added successfully",parent=self.root)
            except Exception as e:
                messagebox.showerror("Error",f"details not added due to :{str(e)}",parent=self.root)
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
