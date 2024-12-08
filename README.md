# Library Management System (Python)

This project is a **Library Management System** built using Python. It features a **Graphical User Interface (GUI)** implemented with the `Tkinter` library and a database powered by **MySQL**. The system includes functionalities for **admin** and **student** users, with secure **JWT authentication** for login sessions.

---

## Features

1. **Admin Panel**:
   - Default admin credentials: **Username:** `admin`, **Password:** `admin`.
   - Admin can manage books in the library, including adding, updating, deleting, and viewing books.

2. **Student Panel**:
   - Students must register (sign up) before logging in.
   - Once logged in, students can view available books and request or issue books.

3. **Database Integration**:
   - **MySQL** database stores user credentials, book details, and admin information.

4. **JWT Authentication**:
   - Secure login for both admin and student users.
   - Tokens include session expiration to ensure secure and temporary access.

5. **GUI Design**:
   - User-friendly graphical interface for smooth interaction.
   - Dynamic windows for admin and student functionalities.

---

## How to Run the Project

### Prerequisites
1. Python 3.8 or higher installed on your system.
2. MySQL server installed and running.
3. Required Python libraries:
   - `mysql-connector-python`
   - `pyjwt`
   - `tkinter`

   Install the libraries with:
   ```bash
   pip install mysql-connector-python pyjwt
