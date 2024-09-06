
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    grade_grades = grades[:]
    total_gpas = sum(grade_grades)
    print(total_gpas)
    num_of_categories = len(grade_grades)
    print(num_of_categories)
    total_modules = 0
    for i in range(num_of_categories):
        total_modules = total_modules + grade_grades[i]
    average = total_gpas / total_modules

    if average < 4.0:
        grade = 'F'
    elif average < 3.7:
        grade = 'D-'
    elif average < 3.3:
        grade = 'D'
    elif average < 3.0:
        grade = 'D+'
    elif average < 2.7:
        grade = 'C-'
    elif average < 2.3:
        grade = 'C'
    elif average < 2.0:
        grade = 'C+'
    elif average < 1.7:
        grade = 'B-'
    elif average < 1.3:
        grade = 'B'
    elif average < 1.0:
        grade = 'B+'
    elif average < 0.7:
        grade = 'A-'
    elif average < 0.0:
        grade = 'A'
    else:
        grade = 'A+'
    print(grade)
    grade_grades.append(grade)
    return grade_grades