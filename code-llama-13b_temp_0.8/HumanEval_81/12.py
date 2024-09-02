
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
    grade_eq = []
    for num in grades:
        if num == 0.0:
            grade_eq.append('E')
        elif num > 0.0 and num <= 1.0:
            grade_eq.append('D-')
        elif num > 1.0 and num <= 1.3:
            grade_eq.append('D')
        elif num > 1.3 and num <= 1.7:
            grade_eq.append('D+')
        elif num > 1.7 and num <= 2.0:
            grade_eq.append('C-')
        elif num > 2.0 and num <= 2.3:
            grade_eq.append('C')
        elif num > 2.3 and num <= 2.7:
            grade_eq.append('C+')
        elif num > 2.7 and num <= 3.0:
            grade_eq.append('B-')
        elif num > 3.0 and num <= 3.3:
            grade_eq.append('B')
        elif num > 3.3 and num <= 3.7:
            grade_eq.append('B+')
        elif num > 3.7 and num <= 4.0:
            grade_eq.append('A-')
        elif num == 4.0:
            grade_eq.append('A')
    return grade_eq
            
