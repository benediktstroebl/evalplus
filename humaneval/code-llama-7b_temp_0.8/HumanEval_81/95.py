
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

    APLUS_CONSTANT = 4.0
    A_CONSTANT = 3.7
    A_MINUS_CONSTANT = 3.3
    BPLUS_CONSTANT = 3.0
    B_CONSTANT = 2.7
    B_MINUS_CONSTANT = 2.3
    CPLUS_CONSTANT = 2.0
    C_CONSTANT = 1.7
    C_MINUS_CONSTANT = 1.3
    DPLUS_CONSTANT = 1.0
    D_CONSTANT = 0.7
    D_MINUS_CONSTANT = 0.0

    results = []

    for gpa in grades:
        if gpa >= APLUS_CONSTANT:
            results.append('A+')
        elif gpa >= A_CONSTANT and gpa < APLUS_CONSTANT:
            results.append('A')
        elif gpa >= A_MINUS_CONSTANT and gpa < A_CONSTANT:
            results.append('A-')
        elif gpa >= BPLUS_CONSTANT:
            results.append('B+')
        elif gpa >= B_CONSTANT and gpa < BPLUS_CONSTANT:
            results.append('B')
        elif gpa >= B_MINUS_CONSTANT and gpa < B_CONSTANT:
            results.append('B-')
        elif gpa >= CPLUS_CONSTANT:
            results.append('C+')
        elif gpa >= C_CONSTANT and gpa < CPLUS_CONSTANT:
            results.append('C')
        elif gpa >= C_MINUS_CONSTANT and gpa < C_CONSTANT:
            results.append('C-')
        elif gpa >= DPLUS_CONSTANT:
            results.append('D+')
        elif gpa >= D_CONSTANT and gpa < DPLUS_CONSTANT:
            results.append('D')
        elif gpa >= D_MINUS_CONSTANT and gpa
