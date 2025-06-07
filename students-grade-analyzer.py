def display_student_summary(names, grades):
    print("Student Summary:")
    for i, name in enumerate(names):
        print(names[i], "-", grades[i])

def get_avg_grade(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades) if len(grades) > 0 else 0

def get_highest_grade(names, grades):
    if not grades:
        return None, 0
    max_grade = grades[0]
    max_index = 0
    for i, grade in enumerate(grades):
        if grades[i] > max_grade:
            max_grade = grades[i]
            max_index = i
    return names[max_index], max_grade

def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count

names = []
grades = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter the student name: ")
    grade = float(input("Enter your grade: "))
    names.append(name)
    grades.append(grade)

display_student_summary(names, grades)
print("Average grade:", get_avg_grade(grades))
top_name, top_grade = get_highest_grade(names, grades)
print("Highest grade:", top_name, "-", top_grade)
print("Number of students who passed:", count_passed(grades))

