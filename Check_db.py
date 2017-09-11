import sqlite3
import sys
import tkinter
window = tkinter.Tk()
con = sqlite3.connect('students.db')
def can_ride():
    print("Getting all students who can ride the rollercoaster...")
    with con:
        cs = con.cursor()
        cs.execute("SELECT Name FROM students WHERE Height >= 1.3 AND Release_form == 1")
        rollercoaster = cs.fetchall()
        for row in rollercoaster:
            print(row[0])
        print("Done!")
def can_ride_needs_form():
    print("Getting all students who can ride the rollercoaster but need a form...")
    with con:
        cs = con.cursor()
        cs.execute("SELECT Name FROM students WHERE Height >= 1.3 AND Release_form == 0")
        rollercoaster = cs.fetchall()
        for row in rollercoaster:
            print(row[0])
        print("Done!")
def cant_ride():
    print("Getting all students who cannot ride the rollercoaster...")
    with con:
        cs = con.cursor()
        cs.execute("SELECT Name FROM students WHERE Height < 1.3")
        rollercoaster = cs.fetchall()
        for row in rollercoaster:
            print(row[0])
        print("Done!")
def needs_form():
    print("Getting all students who need forms...")
    with con:
        cs = con.cursor()
        cs.execute("SELECT Name FROM students WHERE Release_form == 0")
        rollercoaster = cs.fetchall()
        for row in rollercoaster:
            print(row[0])
        print("Done!")
def all_students():
    print("Getting all students...")
    with con:
        cs = con.cursor()
        cs.execute("SELECT Name FROM students WHERE ID >= 0")
        rollercoaster = cs.fetchall()
        for row in rollercoaster:
            print(row[0])
        print("Done!")
        
def callback_can_ride():
    can_ride()
button_can_ride = tkinter.Button(text="View students who can ride", command = callback_can_ride)
button_can_ride.pack()

def callback_can_ride_needs_form():
    can_ride_needs_form()
button_can_ride_form = tkinter.Button(text="View students who could ride but need a consent form", command = callback_can_ride_needs_form)
button_can_ride_form.pack()

def callback_cant_ride():
    cant_ride()
button_cant_ride= tkinter.Button(text="View students who cannot ride", command = callback_cant_ride)
button_cant_ride.pack()

def callback_needs_form():
    needs_form()
button_needs_form= tkinter.Button(text="View students who need a form", command = callback_needs_form)
button_needs_form.pack()

def callback_all_students():
    all_students()
button_all_students= tkinter.Button(text="View all students", command = callback_all_students)
button_all_students.pack()

