from pathlib import Path
import jwt
import datetime
import mysql.connector
from mysql.connector import Error
from tkinter import Tk, messagebox
from admin import admin
from student import student

SECRET_KEY = "dasjiedipaskhrfpasikjfspikhpfpshaifhshfoshd"  # Replace with a strong secret key

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

# Establish database connection and ensure tables exist
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
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user (
                    roll_no INT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS admin (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)
            cur.execute("SELECT * FROM admin WHERE name = 'admin'")
            if not cur.fetchone():  # Insert default admin if it doesn't exist
                cur.execute("INSERT INTO admin (name, password) VALUES (%s, %s)", ('admin', 'admin'))
            conn.commit()
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

# Generate JWT Token
def generate_jwt_token(user_id, user_role):
    payload = {
        "user_id": user_id,
        "role": user_role,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=1),  # Token expires in 1 hour
        "iat": datetime.datetime.now()  # Issued at time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

# Verify JWT Token
def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

# Register a new user
def register_user(rollno, name, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO user (roll_no, name, password) VALUES (%s, %s, %s)", (rollno, name, password))
        conn.commit()
        cur.close()
        conn.close()
        print("User registered successfully!")
    except Error as e:
        print(f"Error: {e}")

# Login as Admin
def admin_login(name, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("SELECT id FROM admin WHERE name = %s AND password = %s", (name, password))
            result = cur.fetchone()
            if result:
                token = generate_jwt_token(user_id=result[0], user_role="admin")
                print("Admin Login Successful! JWT Token:", token)
                window = Tk()
                window.title('Admin_User')
                window.geometry('700x450')
                obj = admin(window)
                window.mainloop()
            else:
                messagebox.showinfo('Error', 'INVALID CREDENTIALS for ADMIN LOGIN')
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

# Login as Student
def student_login(name, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("SELECT roll_no FROM user WHERE name = %s AND password = %s", (name, password))
            result = cur.fetchone()
            if result:
                token = generate_jwt_token(user_id=result[0], user_role="student")
                print("Student Login Successful! JWT Token:", token)
                window = Tk()
                window.title('Student_User')
                window.geometry('700x400')
                obj = student(window)
                window.mainloop()
            else:
                messagebox.showinfo('Error', 'INVALID CREDENTIALS for STUDENT LOGIN')
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")

connect()
def checks(name, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("SELECT roll_no FROM user WHERE name = %s AND password = %s", (name, password))
            result = cur.fetchone()
            if result:
                token = generate_jwt_token(user_id=result[0], user_role="student")
                print(f"Student login successful! JWT Token: {token}")
                window = Tk()
                window.title('Admin_User')
                window.geometry('700x400')
                obj = admin(window)
                window.mainloop()
                # Here, instead of calling the student interface directly, return the token for further processing
                return token
            else:
                messagebox.showinfo("Error", "INVALID CREDENTIALS for STUDENT LOGIN")
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")
        return None


def check(name, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        if conn.is_connected():
            cur = conn.cursor()
            cur.execute("SELECT id FROM admin WHERE name = %s AND password = %s", (name, password))
            result = cur.fetchone()
            if result:
                token = generate_jwt_token(user_id=result[0], user_role="admin")
                print(f"Admin login successful! JWT Token: {token}")
                # Here, instead of calling the admin interface directly, return the token for further processing
                window = Tk()
                window.title('Admin_User')
                window.geometry('700x450')
                obj = admin(window)
                window.mainloop()
                return token
            else:
                messagebox.showinfo("Error", "INVALID CREDENTIALS for ADMIN LOGIN")
            cur.close()
            conn.close()
    except Error as e:
        print(f"Error: {e}")
        return None
    

    