#!/usr/bin/python

from Tkinter import *

def show_entry_fields():
    master = Tk()
    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    currect = float(e1.get())
    weight = float(e2.get())
    #msg = Message(master, text = "Test")
    #msg.config(bg='lightgreen', font=('times', 24, 'italic'))
    #msg.pack( )
    if currect >= 90:
        grade = "A"
    elif currect >= 80:
        grade = "B"
    elif currect >= 70:
        grade = "C"
    elif currect >= 60:
        grade = "D"
    else:
        grade = "F"

    if grade == "A":
        msg = Message(master, text = "To keep your A, you must score a " + str((90 - (currect*(1-weight/100)))/(weight/100)) + "% on the final.")
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack( )
    if grade =="B":
        msg = Message(master, text = "To keep your B, you must score a " + str((80 - (currect*(1-weight/100)))/(weight/100)) + "% on the final.")
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack( )
        if (90 - (currect*(1-weight/100)))/(weight/100) <= 100:
            msg = Message(master, text = "You must score a " + str((90 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to raise your grade to an A.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
        else:
            msg = Message(master, text = "It is not possible to raise your grade to an A.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
    if grade == "C":
        msg = Message(master, text =  "To keep your C, you must score a " + str((70 - (currect*(1-weight/100)))/(weight/100)) + "% on the final.")
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack( )
        if (80 - (currect*(1-weight/100)))/(weight/100) <= 100:
            msg = Message(master, text =  "You must score a " + str((80 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to raise your grade to a B.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
        else:
            msg = Message(master, text = "It is not possible to raise your grade to a B.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
    if grade == "D":
        msg = Message(master, text = "To keep your D, you must score a " + str((60 - (currect*(1-weight/100)))/(weight/100)) + "% on the final.")
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.pack( )
        if (70 - (currect*(1-weight/100)))/(weight/100) <= 100:
            msg = Message(master, text = "You must score a " + str((70 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to raise your grade to a C.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
        else:
            msg = Message(master, text = "It is not possible to raise your grade to a C.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
    if grade == "F":
        if (60 - (currect*(1-weight/100)))/(weight/100) <= 100:
            
            msg = Message(master, text = "You must get a " + str((60 - (currect*(1-weight/100)))/(weight/100)) + "% on the final to get a D.")
            msg.config(bg='lightgreen', font=('times', 24, 'italic'))
            msg.pack( )
        else:
            msg = Message(master, text = "It isn't possible for you to pass this class.")
            msg.config(bg='red', font=('times', 24, 'italic'))
            msg.pack( )
master = Tk()
Label(master, text="What is your current grade percentage?").grid(row=0)
Label(master, text="What percentage of your semester grade is the Final?").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Calculate', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )