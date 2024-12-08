from pathlib import Path
import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
load_dotenv()

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
import os
DB_USER=os.getenv('DB_USER')
DB_HOST=os.getenv('DB_HOST')
DB_PASSWORD=os.getenv('DB_PASSWORD')
DB_PORT=os.getenv('DB_PORT')
DB_NAME=os.getenv('DB_NAME')

def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS BOOK (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255),
                    author VARCHAR(255),
                    year INT,
                    isbn BIGINT
                )
            """)
            conn.commit()
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

def issue():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS issue (
                    id INT NOT NULL,
                    title VARCHAR(255),
                    author VARCHAR(255),
                    year INT,
                    isbn BIGINT,
                    PRIMARY KEY (id)
                )
            """)
            conn.commit()
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

def request():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS request (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(255),
                    author VARCHAR(255),
                    year INT,
                    isbn BIGINT
                )
            """)
            conn.commit()
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

# CRUD operations
def insert(title, author, year, isbn):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO BOOK (title, author, year, isbn) VALUES (%s, %s, %s, %s)", (title, author, year, isbn))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def request_insert(title, author, year, isbn):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO request (title, author, year, isbn) VALUES (%s, %s, %s, %s)", (title, author, year, isbn))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def request_view():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM request")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Error as e:
        print(f"Error: {e}")
        return []

def request_delete(title):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM request WHERE title = %s", (title,))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def issue_delete(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM issue WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def issue_insert(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO issue SELECT * FROM BOOK WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def issue_view():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM issue")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Error as e:
        print(f"Error: {e}")
        return []

def view():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM BOOK")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Error as e:
        print(f"Error: {e}")
        return []

def search(title="", author="", year="", isbn=""):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM BOOK WHERE title = %s OR author = %s OR year = %s OR isbn = %s
        """, (title, author, year, isbn))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Error as e:
        print(f"Error: {e}")
        return []

def delete(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("DELETE FROM BOOK WHERE id = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

def update(id, title, author, year, isbn):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("""
            UPDATE BOOK SET title = %s, author = %s, year = %s, isbn = %s WHERE id = %s
        """, (title, author, year, isbn, id))
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")

connect()
issue()
request()
