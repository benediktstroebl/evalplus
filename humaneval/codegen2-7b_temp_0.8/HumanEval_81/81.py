
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
    letters = []
    for value in grades:
        if value == 0:
            letters.append('E')
        elif value < 3.0:
            letters.append('A+')
        elif value <= 3.7:
            letters.append('A')
        elif value <= 3.3:
            letters.append('A-')
        elif value <= 2.7:
            letters.append('B+')
        elif value <= 2.3:
            letters.append('B')
        elif value <= 2.0:
            letters.append('B-')
        elif value <= 1.7:
            letters.append('C+')
        elif value <= 1.3:
            letters.append('C')
        else:
            letters.append('C-')
    
