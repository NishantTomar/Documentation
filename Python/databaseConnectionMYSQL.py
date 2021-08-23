#install mysql
#create a data base and table in mysql
#install the mysql connector below by running the command in terminal
    #pip install mysql-connector-python

#here in this "college" is database name and "student" is table name
#columns of "student" table are
#roll_no, first_name, last_name, email, age

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kaku",
  database="college"
)

mycursor = mydb.cursor()


class Student:
      
  
    def enterValues(self):
        
        print("---Enter the Student Details---")
        
        self.rollno=int(input("Enter the Roll no:"))
        self.firstname=input("Enter the First Name:")
        self.lastname=input("Enter the Last Name:")
        self.email=input("Enter the Email")
        self.age = int(input("Enter the age"))
        
        #inserting data into student table
        sql = "INSERT INTO student (roll_no, first_name, last_name, email, age) VALUES (%s, %s, %s, %s, %s)"
        val = (self.rollno, self.firstname, self.lastname, self.email, self.age)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.\n")

    def display(self):
        
        print("Displaying data from Database")
        
        mycursor.execute("SELECT * FROM student")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

                    
st_obj=Student()
st_obj.enterValues()
st_obj.display()
