# College Attendance System
# Easy Python Mini Project

attendance = []
FILENAME = "attendance.txt"

# Load data from file
def load_data():
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                attendance.append(line.strip())
    except FileNotFoundError:
        pass

# Save data to file
def save_data():
    with open(FILENAME, "w") as file:
        for record in attendance:
            file.write(record + "\n")

# Check roll number exists
def roll_exists(roll):
    for record in attendance:
        if record.startswith(f"Roll: {roll},"):
            return True
    return False

# Get valid integer roll number
def get_roll():
    while True:
        roll = input("Enter Roll Number: ")
        if roll.isdigit():
            return roll
        else:
            print(" Roll number must be an integer")

# Get valid student name (string only)
def get_name():
    while True:
        name = input("Enter Student Name: ")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print(" Name must contain only letters")

# Mark attendance
def mark_attendance():
    while True:
        roll = get_roll()
        if roll_exists(roll):
            print(" Same roll number are not allow please enter your roll number again\n")
        else:
            break

    name = get_name()

    while True:
        status = input("Present (P) / Absent (A): ").upper()
        if status == "P" or status == "A":
            break
        else:
            print(" Enter only P or A")

    record = f"Roll: {roll}, Name: {name}, Status: {status}"
    attendance.append(record)
    save_data()

    print(" Attendance marked successfully!\n")

# View attendance
def view_attendance():
    if not attendance:
        print(" No attendance records found.\n")
        return

    print("\n Attendance Records")
    for record in attendance:
        print(record)
    print()

# Delete attendance (roll number only)
def delete_attendance():
    roll = get_roll()
    for record in attendance:
        if record.startswith(f"Roll: {roll},"):
            attendance.remove(record)
            save_data()
            print(" Student record deleted successfully.\n")
            return

    print("Roll number not found.\n")

# Main menu
def main_menu():
    load_data()
    while True:
        print("====== College Attendance System ======")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Delete Student by Roll Number")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            delete_attendance()
        elif choice == "4":
            print(" Exiting... Data saved.")
            break
        else:
            print(" Invalid choice\n")

# Run program
main_menu()
