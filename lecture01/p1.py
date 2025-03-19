class student:
    def __init__(self,student_id,name,age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display_info(self):
        print(f"ID: {self.student_id}, 이름: {self.name}, 나이: {self.age}")

class studentmanager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

student1 = student(1, "김철수", 20)
student2 = student(2, "이영희", 21)
student3 = student(3, "박지민", 19)

manager = studentmanager()
manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

print("현재 등록된 학생 목록: ")
manager.display_all_students()

student4 = student(4, "김철수", 20)
manager.add_student(student4)

print("\n학번 4번 하생 추가 후: ")
manager.display_all_students()
