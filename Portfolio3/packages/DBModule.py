import pandas as pd
import sqlite3 as sql



#create function
def create(DB_location,DB_name):
    conn= sql.connect(DB_location + "/" + DB_name + ".db")
    
    
    
#read function
def read(File_location,File_name):
    path = File_location + "/" + File_name + ".csv"
    dataframe = pd.read_csv(path)
    return dataframe
    

    
#write function    
def write(df,tablename):
    
    conn=sql.connect('my_db/port3.db')
    df.to_sql(name= tablename , con=conn)