import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store DEFAULT CHARACTER SET 'utf8'"
        )
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
