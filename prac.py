# ===============================================
# SMART STUDENT GRADE CALCULATOR
# 100% Basic Python - Perfect for First Year Students
# Concepts Used: if-else, loops, lists, functions, file handling
# ===============================================

students = []                       # List to store all students
FILE_NAME = "student_records.txt"   # File to save data

# Function to add a new student
def add_student():
    print("\n" + "="*40)
    print("       ADD NEW STUDENT")
    print("="*40)
    
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    
    print("Enter marks out of 100 for each subject:")
    subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
    marks = []
    
    for sub in subjects:
        while True:
            m = input(f"Enter {sub} marks: ")
            if m.isdigit() and 0 <= int(m) <= 100:
                marks.append(int(m))
                break
            else:
                print("Please enter valid marks (0-100)")
    
    total = sum(marks)
    percentage = total / len(subjects)
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"
    
    result = "PASS" if percentage >= 40 else "FAIL"
    
    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }
    
    students.append(student)
    save_to_file()        # Auto save
    print("\nStudent Record Added Successfully!")
    print(f"Percentage: {percentage}% | Grade: {grade} | Result: {result}")

# Save all students to file
def save_to_file():
    with open(FILE_NAME, "w") as f:
        for s in students:
            marks_str = ",".join(map(str, s["marks"]))
            line = f"{s['name']}|{s['roll']}|{marks_str}|{s['total']}|{s['percentage']}|{s['grade']}|{s['result']}\n"
            f.write(line)

# Load students from file when program starts
def load_from_file():
    global students
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split("|")
                    marks = list(map(int, parts[2].split(",")))
                    students.append({
                        "name": parts[0],
                        "roll": parts[1],
                        "marks": marks,
                        "total": int(parts[3]),
                        "percentage": float(parts[4]),
                        "grade": parts[5],
                        "result": parts[6]
                    })

# View all students
def view_all():
    if not students:
        print("\nNo records found!")
        return
    
    print("\n" + "="*80)
    print("ROLL    NAME               MATH PHY CHE ENG COMP  TOTAL   %       GRADE  RESULT")
    print("="*80)
    for s in students:
        marks_str = "  ".join([f"{m:3}" for m in s["marks"]])
        print(f"{s['roll']:6}  {s['name']:18} {marks_str}  {s['total']:4}  {s['percentage']:6.2f}%  {s['grade']:6}  {s['result']}")

# Search student by roll number
def search_student():
    roll = input("\nEnter Roll Number to search: ")
    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found!")
            print(f"Name       : {s['name']}")
            print(f"Total      : {s['total']}")
            print(f"Percentage : {s['percentage']}%")
            print(f"Grade      : {s['grade']}")
            print(f"Result     : {s['result']}")
            return
    print("Student not found!")

# Show class topper
def show_topper():
    if not students:
        print("\nNo students!")
        return
    top = max(students, key=lambda x: x["percentage"])
    print("\nCLASS TOPPER")
    print(f"Name      : {top['name']}")
    print(f"Roll No   : {top['roll']}")
    print(f"Percentage: {top['percentage']}%")
    print(f"Grade     : {top['grade']}")

# Main Menu
import os
load_from_file()   # Load old data when program starts

while True:
    print("\n" + "="*50)
    print("   SMART STUDENT GRADE CALCULATOR")
    print("="*50)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Show Class Topper")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        show_topper()
    elif choice == "5":
        print("\nThank You! Project by ARYAN SANGANI")
        break
    else:
        print("Invalid choice! Try again.")