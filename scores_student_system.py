from tkinter import*
import sqlite3

#definition for the functions
#to add and clear the database

db=sqlite3.connect("student.db")
cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student_scores(id integer primary key,name text not null,scores integer not null)""")

def add_details():
	newname=sname.get()
	newgrade=sgrade.get()
	cursor.execute("""INSERT INTO student_scores (name,scores) VALUES(?,?)""",(newname,newgrade))
	db.commit()
	sname.delete(0,END)
	sgrade.delete(0,END)
	sname.focus()

def clear_details():
	sname.delete(0,END)
	sgrade.delete(0,END)
	sname.focus()


#gui definition
win=Tk()
win.title("Students Database System:")
win.geometry("350x400")
win.resizable(0,0)

#labels definition
label_1=Label(text='Enter the Student\'s name: ')
label_1.place(x=30,y=35)
sname=Entry(text="")
sname.place(x=150,y=35,width=200,height=25)
sname.focus()


label_2=Label(text='Enter the Student\'s scores: ')
label_2.place(x=30,y=80)
sgrade=Entry(text="")
sgrade.place(x=150,y=80,width=200,height=25)
sgrade.focus()

add_btn=Button(text='Add',command=add_details,bg='blue')
add_btn.place(x=150,y=120,width=75,height=25)


clear_btn=Button(text='Clear',command=clear_details,bg='red')
clear_btn.place(x=250,y=120,width=75,height=25)


db=sqlite3.connect("student.db")
cursor=db.cursor()

win.mainloop()
db.close()