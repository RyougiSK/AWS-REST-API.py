import pyodbc
import pandas as pd

def lambda_handler(event, context):

            connection =  pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
            'Server=52.63.112.33;'
            'Database=SSIS;'
            'UID=sa;'
            'PWD=TChangeh&33plz7@L')

            cursor = connection.cursor()
            cursor.execute('create table [dbo].[Employee] ( EmpID  int, Name varchar(255))')
	        cursor.execute('insert into [dbo].[Employee] (EmpID, Name) values(1, "Joe")')
            records = cursor.fetchall()
            print("Version")
            print(records)
            connection.close()

   
