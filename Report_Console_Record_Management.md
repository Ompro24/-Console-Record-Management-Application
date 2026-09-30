# Assignment 1: Mini Project – Console Record-Management Application

## Student Details

**Student Name:** Om Mahesh Rane  
**Course:** MCA Semester I  
**Subject:** Python Programming & Relational Database  
**Project Title:** Console Record Management System

---

## 1. Introduction

The Console Record Management System is a simple Python application developed to manage student records through the terminal.

The program allows the user to add, view, search, update and delete student records. The records are stored in a JSON file so that they remain available when the program is opened again.

This project was developed to practice the basic Python concepts covered in the assignment.

---

## 2. Objectives

- To create a simple menu-driven Python application.
- To manage student information.
- To use functions for different operations.
- To use lists and dictionaries for storing records.
- To handle invalid input using exception handling.
- To use File I/O for permanent data storage.

---

## 3. Features

The application provides the following options:

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

The program also checks for duplicate roll numbers and displays suitable messages when a record is not found.

---

## 4. Technologies and Concepts Used

### Technologies

- Python
- JSON
- VS Code
- GitHub

### Python Concepts

- Variables and data types
- Lists and dictionaries
- Conditional statements
- For loop
- While loop
- Functions
- Exception handling
- File I/O
- JSON
- Menu-driven programming

---

## 5. Project Structure

```text
Console-Record-Management-Application/
│
├── main.py
├── students.json
├── README.md
├── REPORT.md
└── screenshots/
```

### File Description

**main.py** – Contains the main Python program and functions.

**students.json** – Stores student records.

**README.md** – Contains project information, features, instructions and screenshots.

**REPORT.md** – Contains the assignment documentation.

**screenshots/** – Contains screenshots of the running application.

---

## 6. Data Structure

The program uses a list to store student records.

Each student is represented using a dictionary:

```python
student = {
    "roll": 42,
    "name": "Om Rane",
    "course": "MCA",
    "marks": 85
}
```

Multiple student dictionaries are stored inside a list.

```python
data = [student1, student2, student3]
```

This makes it simple to search, update and delete records.

---

## 7. Working of the Application

When the program starts, it reads existing records from `students.json`.

The main menu is then displayed.

### Add Student

The user enters the roll number, name, course and marks. The program checks whether the roll number already exists. If it does not exist, the record is added and saved.

### View Students

The program uses a `for` loop to go through the list and display each student's details.

### Search Student

The user enters a roll number. The program checks the records and displays the matching student.

### Update Student

The user enters a roll number and then enters the new name, course and marks. The selected record is updated and saved.

### Delete Student

The user enters a roll number. The matching record is removed and the updated data is saved.

### Exit

The program ends when the user selects option 6.

---

## 8. Functions Used

| Function | Purpose |
|---|---|
| `load_data()` | Reads records from the JSON file |
| `save_data()` | Saves records to the JSON file |
| `add_student()` | Adds a new student |
| `view_students()` | Displays all students |
| `search_student()` | Searches by roll number |
| `update_student()` | Updates a student record |
| `delete_student()` | Deletes a student record |

Using separate functions keeps the program easier to read and maintain.

---

## 9. Exception Handling

Exception handling is used when the user enters an invalid number.

For example:

```python
try:
    roll = int(input("Enter roll number: "))
except ValueError:
    print("Enter a valid roll number.")
```

The program also handles cases where the JSON file does not exist or contains invalid data when the application starts.

---

## 10. File I/O and JSON

The project uses Python's built-in `json` module.

`json.load()` is used to read existing records from `students.json`.

`json.dump()` is used to save records after adding, updating or deleting a student.

This means the records are not lost when the program is closed.

---

## 11. Sample Menu

```text
--- Student Record Management ---
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

---

## 12. Sample Working

### Adding a Student

```text
Enter your choice: 1
Enter roll number: 42
Enter name: Om Rane
Enter course: MCA
Enter marks: 85
Student added successfully.
```

### Searching a Student

```text
Enter your choice: 3
Enter roll number: 42

Roll Number: 42
Name: Om Rane
Course: MCA
Marks: 85.0
```

### Updating a Student

```text
Enter your choice: 4
Enter roll number: 42
Enter new name: Om Rane
Enter new course: MCA
Enter new marks: 99
Record updated.
```

---

## 13. Testing

| Test Case | Expected Result | Result |
|---|---|---|
| Add a new student | Student is added | Passed |
| Add duplicate roll number | Duplicate is rejected | Passed |
| View students | Records are displayed | Passed |
| Search existing roll number | Student details are displayed | Passed |
| Search missing roll number | Student not found message | Passed |
| Update student | Record is updated | Passed |
| Delete student | Record is removed | Passed |
| Enter invalid number | Error message is displayed | Passed |
| Exit | Program closes | Passed |

---

## 14. Screenshots

The project repository contains screenshots showing:

- Adding a student
- Viewing student records
- Searching for a student
- Updating a student
- Deleting a student and exiting the program

These screenshots provide evidence that the application was tested through the terminal.

---

## 15. Limitations

This project is a basic console application created for learning purposes.

- It does not have a graphical user interface.
- It uses a local JSON file instead of a database.
- It is intended for simple student record management.
- It does not include user login or multiple users.

---

## 16. Conclusion

This project helped in understanding how basic Python concepts can be combined to create a working application.

The application uses variables, data types, conditions, loops, functions, lists, dictionaries, exception handling and File I/O. JSON storage also demonstrates how information can be saved and loaded between different program runs.

The completed application provides the required record-management operations and demonstrates the Python concepts included in the assignment.

---

## 17. References

- Python documentation for basic Python programming, functions, exceptions and file handling.
- JSON documentation for reading and writing structured data.
- General GitHub project examples were referred to for understanding project organization and documentation. The implementation and content of this project were developed separately for this assignment.
