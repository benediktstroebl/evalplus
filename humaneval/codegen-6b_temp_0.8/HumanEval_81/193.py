
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
    if len(grades) < 1:
        raise AttributeError('There are no grades to grade.')
    try:
        grade = []
        for g in grades:
            if g < 3.3:
                grade.append('D-')
            elif g < 3.0:
                grade.append('D')
            elif g < 2.7:
                grade.append('D+')
            elif g < 2.3:
                grade.append('C-')
            elif g < 2:
                grade.append('C')
            elif g < 1.7:
                grade.append('C+')
            elif g < 1.3:
                grade.append('B-')
            elif g < 1:
                grade.append('B')
            elif g < 0.7:
                grade.append('B+')
            elif g < 0:
                grade.append('A-' or 'E')
            else:
                grade.append('A+')
    except ValueError:
        raise ValueError('Not all values are numbers.')
    return grade
