##Topic of Student Management using mysql 
##by Saurabh kumar Group

import mysql.connector as m
con = m.connect(host ="localhost",user ="root",passwd ="root")
cur = con.cursor()
cur.execute("create database if not exists Student_Management")
cur.execute("use Student_Management")
print('\t\t\t>>>>>>STUDENT MANAGEMENT<<<<<<\t\t\t\n')
def Add ():
    ch = "Yy"
    while ch in 'Yy':
        roll=str(input("enter roll no. of the student : "))
        name=str(input("enter name of the student : "))
        dob=str(input("enter date of birth  of the student : "))
        att=str(input("enter attendence of the student P/A : "))
        t = "create table if not exists Student_data ( Roll_no varchar(15) primary key, Name varchar(20), DOB varchar(20), Attendance varchar(10))"
        cur.execute(t)
        d = "insert into Student_data (Roll_no, name, DOB, Attendance) values ('"+roll+"','"+name+"','"+dob+"','"+att+"')"
        cur.execute(d)
        con.commit()
        ch = input("do you want to continue adding student ? [y/n] : ")


def Search ():
    ch='Yy'
    while ch in 'Yy':
        x=int(input(" ================================= \n [1] search by rollno. \n [2] search by name \n [3] search by date of birth \n [4] search present student \n [5] search absent student \n  =================================\n:"))
        if x==1 :
            print("==================== \n [1] search by rollno. \n====================")
            r=str(input("Enter roll no. of student :"))
            cur.execute("select * from Student_data where Roll_no='"+r+"'")
            record2 = cur.fetchall()
            print("\n ========================================\n || Roll_no || Name || DOB || Attendance ||")
            for i in record2:
                print(i)
            print('========================================\n')
        elif x==2 :
            print("==================== \n [2] search by name \n====================")
            n=str(input("Enter name of student :"))
            cur.execute("select * from Student_data where name='"+n+"'")
            record3 = cur.fetchall()
            print("\n ========================================\n || Roll_no || Name || DOB || Attendance ||")
            for i in record3:
                print(i)
            print('========================================\n')
        elif x==3 :
            print("==================== \n [3] search by birth year \n====================")
            b=str(input("Enter birth year of student :"))
            cur.execute("select * from Student_data where DOB='"+b+"'")
            record4 = cur.fetchall()
            print("\n ========================================\n || Roll_no || Name || DOB || Attendance ||")
            for i in record4:
                print(i)
            print('========================================\n')
        elif x==4 :
            print("==================== \n [4] search present student \n====================")
            cur.execute("select * from Student_data where Attendance='P'")
            record5 = cur.fetchall()
            print("\n ========================================\n || Roll_no || Name || DOB || Attendance ||")
            for i in record5:
                print(i)
            print('========================================\n')
        elif x==5 :
            print("==================== \n [5] search absent student \n====================")
            cur.execute("select * from Student_data where Attendance='A'")
            record6 = cur.fetchall()
            print("\n ========================================\n || Roll_no || Name || DOB || Attendance ||")
            for i in record6:
                print(i)
            print('========================================\n')
        ch = input("\ndo you want to continue searching student ? [y/n] : ")


def Display ():
    cur.execute('select * from student_data;')
    a=cur.fetchall()
    print("\n ========================================\n || Roll_no || Name || DOB || Attendance ||")
    for i in a:
        print(i)
    print('========================================\n')

       
def User ():
    y=int(input("====================================\n press [1] for Adding new student \n press [2] for searching student \n  press [3] to display all data \n press [4] to end program \n====================================\n   :"))
    if y==1:
        Add()
        User()
    elif y==2:
        Search()
        User()
    elif y==3:
        Display()
        User()
    elif y==4:
        print('Program End')
User()

    
