import sqlite3
import os
from pkgutil import read_code


def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn=sqlite3.connect("students.db")
    cursor=conn.cursor()
    return conn,cursor
def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        age INTEGER,
        email VARCHAR UNIQUE,
        city VARCHAR) 
''')
    cursor.execute('''
                   CREATE TABLE Courses
                   (
                       id    INTEGER PRIMARY KEY,
                       course_name  VARCHAR NOT NULL,
                       insturctor VARCHAR TEXT,
                       credits  INTEGER
                   )
                   ''')




def insert_sample_data(cursor):
    students=[
        (1,'Ayse Yılmaz',20,'ayse@gmail','New York'),
        (2, 'Ferhat Kılmaz', 16, 'ferhat@gmail', 'Ankara'),
        (3, 'Ece Kara', 21, 'ece@gmail', 'Malatya'),
        (4, 'İlo Çelikkaya', 30, 'ilo@gmail', 'İzmir'),
        (5, 'Omer Yılmaz', 34, 'omer@gmail', 'Boston')
    ]
    cursor.executemany("INSERT INTO Students VALUES(?,?,?,?,?)",students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)
    print("Sample data inserted successfully")


def basic_sql_operations(cursor):
    #1-select all
    print("SELECT ALL")
    cursor.execute('SELECT * FROM Students')
    records=cursor.fetchall()
    for i in records:
        print(i)

    print("SELECT COLUMNS")
    #2-select columns
    cursor.execute("SELECT name,age FROM Students")
    records=cursor.fetchall()
    print(records)


    print("WHERE CLAUSE")
    #3-WHERE CLAUSE
    cursor.execute("SELECT * FROM Students WHERE age>=30")
    records=cursor.fetchall()
    print(records)

    print("WHERE WITH STRING")
    # 3-WHERE STRING
    cursor.execute("SELECT * FROM Students WHERE city='Malatya'")
    records = cursor.fetchall()
    print(records)

    print("ORDER BY")
    # 3-ORDER BY
    cursor.execute("SELECT * FROM Students WHERE age>=30 ORDER BY id DESC")
    records = cursor.fetchall()
    for row in records:
     print(row)
     print("LIMIT")
     # 3-WHERE CLAUSE
     cursor.execute("SELECT * FROM Students LIMIT 3")
     records = cursor.fetchall()
     print(records)




def sql_update_delete_insert_operations(conn,cursor):
    #1-INSERT
    cursor.execute("INSERT INTO Students VALUES(6,'Frank Miller',23,'frank@gmail.com','Miami')")
    conn.commit()
    #2-UPDATE
    cursor.execute("UPDATE Students SET age=20 WHERE id=6")
    conn.commit()
    #3-DELETE
    cursor.execute("DELETE FROM Students WHERE id=6")
    conn.commit()
def aggreage_functions(cursor):
    #1-)Count
    print("AGGREGATE FUNCTIONS")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result=cursor.fetchone()
    print(result[0])
    #2-Average
    cursor.execute("SELECT AVG(age) FROM Students")
    result=cursor.fetchone()
    print(result[0])
    # 3) MAX - MIN
    print("----------Aggregate Functions Max-Min----------")
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    max_age, min_age = result
    print(max_age)
    print(min_age)

    # 4) GROUP BY
    print("----------Aggregate Functions Group by----------")
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result = cursor.fetchall()
    print(result)


def questions(cursor):
    '''
    Basit
    1) Bütün kursların bilgilerini getirin
    2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    3) Sadece 21 yaşındaki öğrencileri getirin
    4) Sadece Malatya'da yaşayan öğrencileri getirin
    5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    7) Sadece 3 ve üzeri kredi olan dersleri getirin

    Detaylı
    1) Öğrencileri alphabetic şekilde dizerek getirin
    2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    3) Sadece 'İzmir' veya 'Bostonda' da yaşayan öğrencileri getirin
    4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    '''
    print("Basit")
    print("-QUESTION 1-")
    cursor.execute("SELECT * FROM courses")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 2-")
    cursor.execute("SELECT course_name,insturctor FROM courses")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 3-")
    cursor.execute("SELECT * FROM Students WHERE age=16")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 4-")
    cursor.execute("SELECT * from Students WHERE city='Malatya'")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 5-")
    cursor.execute("SELECT course_name from courses where insturctor='Dr. Anderson'")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 6-")
    cursor.execute("SELECT * from students where name LIKE 'A%'")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 7-")
    cursor.execute("SELECT course_name from courses where credits>=3")
    result=cursor.fetchall()
    print(result)

    print("Detaylı")
    print("-QUESTION 1-")
    cursor.execute("SELECT * from students ORDER BY name ASC")
    result=cursor.fetchall()
    print(result)

    print("-QUESTION 2-")
    cursor.execute("SELECT name From students WHERE age>=20 ORDER BY name ASC ")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 3-")
    cursor.execute("SELECT * FROM Students Where city='Boston' or city='İzmir'")
    result=cursor.fetchall()
    print(result)
    print("-QUESTION 4-")
    cursor.execute("Select * FROM Students WHERE city!='New York'")
    result=cursor.fetchall()
    print(result)
def main():
    conn,cursor=create_database()
    try:
      create_tables(cursor)
      insert_sample_data(cursor)
      basic_sql_operations(cursor)
      sql_update_delete_insert_operations(conn,cursor)
      aggreage_functions(cursor)
      questions(cursor)
      conn.commit()
      #Veritabanına yapılan değişiklikleri kalıcı olarak kaydeder.


    except sqlite3.Error as e:
      print(e)
    finally:
        conn.close() #ne olursa olsn db baglantısını kapat


if __name__=='__main__':
    main()

