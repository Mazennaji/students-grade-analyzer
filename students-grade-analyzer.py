def display_student_summary(name,grades):
    print("Student Summary : ")
    for i in range(len(name)):
        print(name[i] , " - " , grades[i])


def get_avg_grade(grades):
    total =0
    for grade in grades:
        total+=grade
    return total/len(grades)

def get_heighest_grade(name,grades):
    max=grades[0]
    index=0
    for i in range(1,len(grades)):
        max=grades[i]
        index = i
    return name[index],max

def count_passed(name,grades):
    count =0
    for grade in grades:
        if grade>=60:
            count+=1
    return count

name=[]
grade=[]

n=input("Enter number of students : ")

for i in range(n):
    names=input("Enter the student name : ")
    grades=input("Enter your grade : ")
    name.append(names)
    grade.append(grades)

display=display_student_summary(names, grades)
print(display)
print("Average grade:", get_avg_grade(grades))
top_student_grade=get_heighest_grade(names,grades)
print("The highest grade in class: " , top_student_grade)
print("Number of students who passed:", count_passed(grades))

