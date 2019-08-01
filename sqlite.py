"""CRUD operations"""
import sqlite3

class sql_operation:
    
    def __init__(self):
        self.conn = sqlite3.connect('test.db')
        print("Opened database successfully")

    def list_all_tables(self):
        print("all tables are")
        cursor = self.conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for i in cursor:
            print(i)

    def create_table(self):
        """create table"""
        self.conn.execute("""CREATE TABLE IF NOT EXISTS COMPANY (
                 ID             INT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 AGE            INT     NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL);""")
        print("Table  Company created successfully")
        self.conn.commit()

    def create_temporary_table(self):
        """create table"""
        self.conn.execute("""CREATE TEMPORARY TABLE IF NOT EXISTS COMPANY (
                 ID             INT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 AGE            INT     NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL)""")
        print("Table  Company created successfully")
        self.conn.commit()

    def get_column_names_in_table(self):
        cursor = self.conn.execute("SELECT * FROM COMPANY")
        col_names = [row[0] for row in cursor.description]
        print(col_names)

    def read_table(self):
        """READ"""
        cursor = self.conn.execute("SELECT id, name, address, salary from COMPANY LIMIT 2")
        for row in cursor:
           print( "ID = ", row[0])
           print( "NAME = ", row[1])
           print( "ADDRESS = ", row[2])
           print( "SALARY = ", row[3], "\n")

    def update_table(self):
        """Update"""
        self.conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
        self.conn.commit
        print ("Total number of rows updated :", self.conn.total_changes)
        
        cursor = self.conn.execute("SELECT id, name, address, salary from COMPANY")
        for row in cursor:
           print( "ID = ", row[0])
           print( "NAME = ", row[1])
           print( "ADDRESS = ", row[2])
           print( "SALARY = ", row[3], "\n")        
        print("Updated records successfully")
        self.conn.commit()
        
    def insert_table(self):
        """Insert"""        
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )");
        
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
        
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
        
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
        print("Records inserted into company successfully")
        self.conn.commit()

    
    def delete_records(self):
        """delete records"""
        self.conn.execute("DELETE FROM COMPANY WHERE SALARY = 25000.00 AND ID = 1")
        self.conn.commit

    def drop_table(self):
        """Drop table"""
        self.conn.execute(""" DROP TABLE IF EXISTS COMPANY; """)
        print("Table droped successfully")
        self.conn.commit()

    def close_conn(self):
        self.conn.close()
        print("connection closed")
    
if __name__ == "__main__":
    sql = sql_operation()
    sql.drop_table()
    sql.create_table()
    sql.list_all_tables()
    sql.insert_table()
    sql.read_table()
    sql.get_column_names_in_table()
    sql.close_conn()
