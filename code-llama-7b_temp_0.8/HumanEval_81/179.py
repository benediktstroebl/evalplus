
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
    a_plus_grades = (4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9)
    a_minus_grades = (3.7, 3.8, 3.9)
    a_grades = (3.0, 3.1, 3.2, 3.3)
    b_plus_grades = (2.8, 2.9)
    b_grades = (2.0, 2.1, 2.2, 2.3)
    b_minus_grades = (1.8, 1.9)
    c_plus_grades = (1.7, 1.8, 1.9)
    c_grades = (1.0, 1.1, 1.2, 1.3)
    d_plus_grades = (0.9, 0.99, 0.0)
    d_grades = (0.7, 0.8, 0.79)
    d_minus_grades = (0.0, 0.6, 0.69)

    letter_grades = []

    for grade in grades:
        if grade in a_plus_grades:
            letter_grades.append('A+')
        elif grade in a_minus_grades:
            letter_grades.append('A-')
        elif grade in a_grades:
            letter_grades.append('A')
        elif grade in b_plus_grades:
            letter_grades.append('B+')
        elif grade in b_grades:
            letter_grades.append('B')
        elif grade in b_minus_grades:
            letter_grades.append('B-')
        elif grade in c_plus_grades:
            letter_grades.append('C+')
        elif grade in c_grades:
            letter_grades.append('C')
        elif grade in d_plus_grades:
