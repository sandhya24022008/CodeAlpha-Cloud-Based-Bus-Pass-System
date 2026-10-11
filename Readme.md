
# Cloud-Based Bus Pass System

## Project Overview
The Cloud-Based Bus Pass System is a web application developed using Python and Flask. It allows users to apply for bus passes online and view submitted applications.

## Features
- Online bus pass application
- Passenger details validation
- Daily, Monthly, and Student pass types
- SQLite database for storing applications
- View submitted applications and their status
- Database records remain available when the application restarts, provided the database file is retained

## Technologies Used
- Python
- Flask
- HTML
- SQLite

## Project Structure
- app.py - Main application
- requirements.txt - Python dependencies
- templates/index.html - Home page
- templates/apply.html - Application form
- templates/passes.html - Application list

## How to Run

1. Install Python.
2. Install the required packages:

   pip install -r requirements.txt

3. Start the application:

   python app.py

4. Open your browser and visit:

   http://127.0.0.1:5000

## Database
SQLite stores the submitted bus pass applications. The application uses parameterized SQL queries to help prevent SQL injection.

## Important Note
This is a beginner-friendly prototype. For production cloud deployment, configure persistent database storage, secure secrets, HTTPS, authentication, and access controls.

## Author
Sandhya S
