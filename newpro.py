# student management system example with bugs

students = []

def add_student(name, age):
    # bug: no validation for empty name or negative age
    student = {"name": name, "age": age}
    students.append(student)

def find_student(name):
    # bug: inefficient search
    for s in students:
        if s["name"] == name:
            return s
    return None

def calculate_average_age():
    # bug: division by zero possible
    total = 0
    for s in students:
        total += s["age"]
    return total / len(students)

def remove_student(name):
    # bug: modifying list during iteration
    for s in students:
        if s["name"] == name:
            students.remove(s)

def print_students():
    # code smell: unused variable
    count = 0
    for s in students:
        print("Student:", s["name"], "Age:", s["age"])

# duplicate code smell
def show_students():
    for s in students:
        print("Student:", s["name"], "Age:", s["age"])


# main program
add_student("Ali", 20)
add_student("Sara", 19)
add_student("", -5)   # invalid data but accepted

print_students()

avg = calculate_average_age()
print("Average age:", avg)

remove_student("Ali")
show_students()