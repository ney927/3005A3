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

cursor.execute("DROP TABLE IF EXISTS students;")

createTable = """CREATE TABLE IF NOT EXISTS students( 
    student_id  SERIAL PRIMARY KEY,
    first_name  VARCHAR(255)   NOT NULL,
    last_name   VARCHAR(255)   NOT NULL,
    email   VARCHAR(255)   UNIQUE   NOT NULL,
    enrollment_date DATE
);"""
cursor.execute(createTable)

insertDate = """INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');"""
cursor.execute(insertDate)

print("students table created with initial data.")

conn.close()