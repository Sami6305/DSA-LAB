class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.attendance = "Absent"
        self.next = None


class AttendanceTracker:
    def __init__(self):
        self.head = None

    def add_student(self, roll_no, name):
        new_student = Student(roll_no, name)
        if not self.head:
            self.head = new_student  # If the list is empty, make this the first student
        else:
            current = self.head
            while current.next:  # Traverse until the last student in the list
                current = current.next
            current.next = new_student  # Add the new student to the end
        print(f"Student {name} added successfully.")

    def mark_present(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.attendance = "Present"
                print(f"Attendance marked 'Present' for Roll No: {roll_no}.")
                return
            current = current.next
        print(f"Student with Roll No {roll_no} not found.")

    def mark_absent(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                current.attendance = "Absent"
                print(f"Attendance marked 'Absent' for Roll No: {roll_no}.")
                return
            current = current.next
        print(f"Student with Roll No {roll_no} not found.")

    def delete_student(self, roll_no):
        current = self.head
        prev = None
        while current:
            if current.roll_no == roll_no:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Student with Roll No {roll_no} deleted successfully.")
                return
            prev = current
            current = current.next
        print(f"Student with Roll No {roll_no} not found.")

    def search_student(self, roll_no):
        current = self.head
        while current:
            if current.roll_no == roll_no:
                print(f"Student Found: Roll No: {current.roll_no}, Name: {current.name}, Attendance: {current.attendance}")
                return
            current = current.next
        print(f"Student with Roll No {roll_no} not found.")

    def display_students(self):
        if not self.head:
            print("No students found.")
            return
        print("\n--- Student Attendance List ---")
        current = self.head
        while current:
            print(f"Roll No: {current.roll_no}, Name: {current.name}, Attendance: {current.attendance}")
            current = current.next
        print("-------------------------------\n")

    def sort_students(self):
        if not self.head or not self.head.next:
            print("Not enough students to sort.")
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.roll_no > current.next.roll_no:
                    current.roll_no, current.next.roll_no = current.next.roll_no, current.roll_no
                    current.name, current.next.name = current.next.name, current.name
                    current.attendance, current.next.attendance = current.next.attendance, current.attendance
                    swapped = True
                current = current.next
        print("Students sorted by Roll No successfully.")


def main():
    tracker = AttendanceTracker()

    while True:
        print("\n===== Attendance Tracker Menu =====")
        print("1. Add New Student")
        print("2. Mark Student Present")
        print("3. Mark Student Absent")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Display All Students")
        print("7. Sort Students by Roll No")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            try:
                roll_no = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                tracker.add_student(roll_no, name)
            except ValueError:
                print("Invalid Roll Number. Please enter a valid number.")

        elif choice == '2':
            try:
                roll_no = int(input("Enter Roll Number to mark present: "))
                tracker.mark_present(roll_no)
            except ValueError:
                print("Invalid Roll Number. Please enter a valid number.")

        elif choice == '3':
            try:
                roll_no = int(input("Enter Roll Number to mark absent: "))
                tracker.mark_absent(roll_no)
            except ValueError:
                print("Invalid Roll Number. Please enter a valid number.")

        elif choice == '4':
            try:
                roll_no = int(input("Enter Roll Number to delete: "))
                tracker.delete_student(roll_no)
            except ValueError:
                print("Invalid Roll Number. Please enter a valid number.")

        elif choice == '5':
            try:
                roll_no = int(input("Enter Roll Number to search: "))
                tracker.search_student(roll_no)
            except ValueError:
                print("Invalid Roll Number. Please enter a valid number.")

        elif choice == '6':
            tracker.display_students()

        elif choice == '7':
            tracker.sort_students()

        elif choice == '8':
            print("Exiting Attendance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


main()
