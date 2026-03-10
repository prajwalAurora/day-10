class Student:
    college_name = "ABC College"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Student object created")

s1 = Student("Alice", 20)
print(s1.name)  # Output: Alice