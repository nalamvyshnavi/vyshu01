import pyodbc
server = 'HCL-02-73\SQLEXPRESS'
database = 'employee_table'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
#print(cnxn)
cursor = cnxn.cursor()
#print(cursor)
class Exits(Exception):
    pass
class employee_schema:
    def employee_details(self):
        try:
            details=cursor.execute('''select *from employee_table1''')
            if(not(details)):
                query=cursor.execute('''use employee_table ''')
                query1=cursor.execute(''' create table employee_table
                                (
                                nameofemployee varchar(50),
                                salary int,
                                project varchar(50)
                                )
                                ''')
                query2=cursor.execute('''select *from employee_table1''')
        #INSERT INTO employee_table (nameofemployee,salary,project)
        #vALUES
                cnxn.commit()
            else:
                raise Exits
        except Exits:
            print("Table exits in DB")


#obj=employeeschema()
#obj.employee_details()


