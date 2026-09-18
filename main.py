import json

FILE = "students.json"


# Read records from the file
def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save records to the file
def save_data(data):
    try:
        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)
    except OSError:
        print("Error while saving the file.")


# Add a new student
def add_student(data):
    try:
        roll = int(input("Enter roll number: "))

        # Check if the roll number already exists
        for student in data:
            if student["roll"] == roll:
                print("Roll number already exists.")
                return

        name = input("Enter name: ")
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        student = {
            "roll": roll,
            "name": name,
            "course": course,
            "marks": marks
        }

        data.append(student)
        save_data(data)

        print("Student added successfully.")

    except ValueError:
        print("Please enter valid values.")


# Display all student records
def view_students(data):
    if not data:
        print("No records found.")
        return

    for student in data:
        print("\nRoll Number:", student["roll"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])


# Search a student by roll number
def search_student(data):
    try:
        roll = int(input("Enter roll number: "))

        for student in data:
            if student["roll"] == roll:
                print("\nRoll Number:", student["roll"])
                print("Name:", student["name"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])
                return

        print("Student not found.")

    except ValueError:
        print("Enter a valid roll number.")


# Update an existing student
def update_student(data):
    try:
        roll = int(input("Enter roll number: "))

        for student in data:
            if student["roll"] == roll:
                name = input("Enter new name: ")
                course = input("Enter new course: ")
                marks = float(input("Enter new marks: "))

                student["name"] = name
                student["course"] = course
                student["marks"] = marks

                save_data(data)

                print("Record updated.")
                return

        print("Student not found.")

    except ValueError:
        print("Enter valid values.")


# Delete a student record
def delete_student(data):
    try:
        roll = int(input("Enter roll number: "))

        for student in data:
            if student["roll"] == roll:
                data.remove(student)
                save_data(data)

                print("Record deleted.")
                return

        print("Student not found.")

    except ValueError:
        print("Enter a valid roll number.")


data = load_data()

# Main menu
while True:
    print("\n--- Student Record Management ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(data)

    elif choice == "2":
        view_students(data)

    elif choice == "3":
        search_student(data)

    elif choice == "4":
        update_student(data)

    elif choice == "5":
        delete_student(data)

    elif choice == "6":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")
