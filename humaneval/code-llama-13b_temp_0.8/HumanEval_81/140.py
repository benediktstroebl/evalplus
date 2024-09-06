
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
    grades = [str(grade) for grade in grades]
    grades = [grade[0]+'.0' if float(grade) > 4.0 else grade for grade in grades]
    table = {
        'A+': 4.0, 
        'A' : 3.7, 
        'A-': 3.3, 
        'B+': 3.0, 
        'B' : 2.7, 
        'B-': 2.3, 
        'C+': 2.0, 
        'C' : 1.7, 
        'C-': 1.3, 
        'D+' : 1.0, 
        'D' : 0.7, 
        'D-': 0.3, 
        'E' : 0.0
    }
    letter_grades = []
    for grade in grades:
        if float(grade) >= 3.7:
            letter_grades.append(min(table, key=lambda key: abs(float(key)-float(grade))))
        else:
            letter_grades.append('E')
    return letter_grades

