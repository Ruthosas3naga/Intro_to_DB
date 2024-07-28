# import mysql.connector

# def create_database ()
# mydb = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Iamjesuloba11@#"
#             database = "alx_book_store"  # Replace with your MySQL root password
#         );
# print(mydb.get_server_info())
import mysql.connector
from mysql.connector import errorcode

def create_database(cursor, db_name):
    try:
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET 'utf8'"
        )
        print(f"Database '{db_name}' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")

def main():
    db_name = "alx_book_store"
    
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nagastic11@#"  # Replace with your MySQL root password
        )
        cursor = cnx.cursor()
        create_database(cursor, db_name)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor.close()
        cnx.close()

if __name__ == "__main__":
    main()
