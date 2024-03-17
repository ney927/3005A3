import psycopg2

#connect the to database
conn = psycopg2.connect(
    database = 'A3',
    user = 'postgres',
    password = 'awesomeNKB927',
    host = 'localhost',
    port = '5432'
)

conn.autocommit = True
cursor = conn.cursor()

# retrieves and displays all records from the student table
def getAllStudents():
    cursor.execute("select * from students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Inserts a new student record into the students table.
def addStudent(fname, lname, email, date):
    insertStudent = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{fname}', '{lname}', '{email}', '{date}');"
    cursor.execute(insertStudent)

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(id, email):
    updateStudent = f"UPDATE students SET email = '{email}' WHERE student_id = {id}"
    cursor.execute(updateStudent)

# Deletes the record of the student with the specified student_id.
def deleteStudent(id):
    deleteStudent = f"DELETE FROM students WHERE student_id = {id}"
    cursor.execute(deleteStudent)

# prints the menu of actions the user can do
def menu():
    print("""\nMENU: 
1) Get all Students 
2) Add Student 
3) Update Student Email 
4) Delete Student
enter the number of the function you wish to execute
or enter BYEBYE to exit the application\n""")


exit = False
menu() #prints the menu
userInput = input() #gets user input

#calls the appropriate function based on the user input
if (userInput == '1'):
    getAllStudents()
elif (userInput == '2'):
    # ask the user for the details of the student you want to create
    fname = input ("Enter the new student's first name: ")
    lname = input ("Enter the new student's last name: ")
    email = input ("Enter the new student's email: ")
    date = input ("Enter the new student's enrollment date (YYYY-MM-DD): ")
    addStudent(fname, lname, email, date)

    # print the record of the new student
    cursor.execute(f"SELECT * from students WHERE email = '{email}';")
    print("student created: ", cursor.fetchone())
elif (userInput == '3'):
    # ask the user for the details of the student you want to update
    id = input ("Enter the id of the student you want to update: ")
    email = input ("Enter the student's new email: ")
    updateStudentEmail(id, email)

    # print the updated record of the student
    cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
    print("student updated: ", cursor.fetchone())
elif (userInput == '4'):
    # get the record id of the student you want to delete
    id = input ("Enter the id of the student you want to delete: ")
    cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
    student = cursor.fetchone()
    deleteStudent(id)

    #print the deleted student record
    print("student deleted", student)
elif (userInput == "BYEBYE"): 
    exit = True

# while the user chooses not to exit, continue completing actions based on user inpu
while (not exit):
    cont = input("enter c to continue... ")

    menu() #prints the menu
    userInput = input() #gets user input

    #calls the appropriate function based on the user input
    if (userInput == '1'):
        getAllStudents()
    elif (userInput == '2'):
        # ask the user for the details of the student you want to create
        fname = input ("Enter the new student's first name: ")
        lname = input ("Enter the new student's last name: ")
        email = input ("Enter the new student's email: ")
        date = input ("Enter the new student's enrollment date (YYYY-MM-DD): ")
        addStudent(fname, lname, email, date)

        # print the record of the new student
        cursor.execute(f"SELECT * from students WHERE email = '{email}';")
        print("student created: ", cursor.fetchone())
    elif (userInput == '3'):
        # ask the user for the details of the student you want to update
        id = input ("Enter the id of the student you want to update: ")
        email = input ("Enter the student's new email: ")
        updateStudentEmail(id, email)

        # print the updated record of the student
        cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
        print("student updated: ", cursor.fetchone())
    elif (userInput == '4'):
        # get the record id of the student you want to delete
        id = input ("Enter the id of the student you want to delete: ")
        cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
        student = cursor.fetchone()
        deleteStudent(id)

        #print the deleted student record
        print("student deleted", student)
    elif (userInput == "BYEBYE"): 
        exit = True

print("\nbyebye!")

conn.close()



