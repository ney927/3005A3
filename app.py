import psycopg2
conn = psycopg2.connect(
    database = 'A3',
    user = 'postgres',
    password = 'awesomeNKB927',
    host = 'localhost',
    port = '5432'
)

conn.autocommit = True
cursor = conn.cursor()


def getStudents():
    cursor.execute("select * from students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def addStudent(fname, lname, email, date):
    insertStudent = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{fname}', '{lname}', '{email}', '{date}');"
    cursor.execute(insertStudent)

def updateStudentEmail(id, email):
    updateStudent = f"UPDATE students SET email = '{email}' WHERE student_id = {id}"
    cursor.execute(updateStudent)

def deleteStudent(id):
    deleteStudent = f"DELETE FROM students WHERE student_id = {id}"
    cursor.execute(deleteStudent)

def menu():
    print("""\nMENU: 
1) Get all Students 
2) Add Student 
3) Update Student Email 
4) Delete Student
enter the number of the function you wish to execute
or enter BYEBYE to exit the application\n""")


exit = False
menu()
userInput = input()
if (userInput == '1'):
    getStudents()
elif (userInput == '2'):
    fname = input ("Enter the new student's first name: ")
    lname = input ("Enter the new student's last name: ")
    email = input ("Enter the new student's email: ")
    date = input ("Enter the new student's enrollment date (YYYY-MM-DD): ")
    addStudent(fname, lname, email, date)
    cursor.execute(f"SELECT * from students WHERE email = '{email}';")
    print("student created: ", cursor.fetchone())
elif (userInput == '3'):
    id = input ("Enter the id of the student you want to update: ")
    email = input ("Enter the student's new email: ")
    updateStudentEmail(id, email)
    cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
    print("student created: ", cursor.fetchone())
elif (userInput == '4'):
    id = input ("Enter the id of the student you want to delete: ")
    cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
    student = cursor.fetchone()
    deleteStudent(id)
    print("student deleted", student)
elif (userInput == "BYEBYE"):
    exit = True

while (not exit):
    cont = input("enter c to continue... ")

    menu()
    userInput = input()
    if (userInput == '1'):
        getStudents()
    elif (userInput == '2'):
        fname = input ("Enter the new student's first name: ")
        lname = input ("Enter the new student's last name: ")
        email = input ("Enter the new student's email: ")
        date = input ("Enter the new student's enrollment date (YYYY-MM-DD): ")
        addStudent(fname, lname, email, date)
        cursor.execute(f"SELECT * from students WHERE email = '{email}';")
        print("student created: ", cursor.fetchone())
    elif (userInput == '3'):
        id = input ("Enter the id of the student you want to update: ")
        email = input ("Enter the student's new email: ")
        updateStudentEmail(id, email)
        cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
        print("student created: ", cursor.fetchone())
    elif (userInput == '4'):
        id = input ("Enter the id of the student you want to delete: ")
        cursor.execute(f"SELECT * from students WHERE student_id = '{id}';")
        student = cursor.fetchone()
        deleteStudent(id)
        print("student deleted", student)
    elif (userInput == "BYEBYE"):
        exit = True

print("\nbyebye!")

conn.close()