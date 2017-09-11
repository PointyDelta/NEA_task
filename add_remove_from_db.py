import sqlite3
import sys
con = sqlite3.connect('students.db')
global student_complete_data
global next_step
next_step = False
student_complete_data = []
def get_data(next_step):
    next_step = False
    global student_complete_data
    while next_step == False:
        try:
            student_id = int(input("Enter an ID"))
            next_step = True
        except:##will obviously throw exception where str is invalid to be converted into int
            print("Invalid input.")
            next_step = False
    while next_step == True:
            s_name = input("Enter a name")
            if len(s_name) == 0:
                print("Uh oh, looks like you've accidentally left this field blank. Please enter a name.")
                next_step = True
            else:
                next_step = False
            
    while next_step == False:
        try:
            s_height = float(input("Enter a height"))
            break
        except:
            print("Uh oh, looks like you've accidentally entered an invalid number. Please enter a height.")
            next_step = False
    release_form = input("Signed release form? (y/n)")
    while True:#check it's one of the two acceptable inputs, triggers this loop until it is
        if release_form == "y":
            break
        if release_form == "n":
            break
        print("Invalid input. Please enter either 'y' or 'n'")
        release_form = input("Signed release form? (y/n)")  
    release_form = release_form == "y"
    student_complete_data = [student_id, s_name, s_height, release_form]

def to_database(student_complete_data):
    conf = input("Confirm commit to database? (y/n)") == "y"
    if conf == True:
        with con:
            cs = con.cursor()
            cs.execute("INSERT INTO students VALUES (?,?,?,?)",(student_complete_data[0], student_complete_data[1], student_complete_data[2], student_complete_data[3]))
            print("Done!")
            print(student_complete_data,"inserted into database")
    else:
        print("Made an error? Going back to data input.")
        get_data(next_step)
get_data(next_step)
to_database(student_complete_data)
