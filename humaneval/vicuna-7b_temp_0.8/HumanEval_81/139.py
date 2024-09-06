
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
    if not grades:
        return []
    
    # sort the list of GPAs
    grades.sort()
    
    # create a list to store the letter grades
    letter_grades = []
    
    # determine the number of A+, A, A-, etc.
    num_a_pluses = 0
    for grade in grades:
        if grade >= 4.0 and grade <= 4.25:
            num_a_pluses += 1
        else:
            num_a_pluses = 0
    
    # determine the number of B+, B, B-, etc.
    num_b_pluses = 0
    num_b_minus = 0
    for grade in grades:
        if grade >= 3.0 and grade <= 3.24:
            num_b_pluses += 1
        else:
            if grade < 3.0:
                num_b_minus += 1
            else:
                num_b_pluses += 1
    
    # determine the number of C+, C, C-, etc.
    num_c_pluses = 0
    num_c_minus = 0
    for grade in grades:
        if grade >= 2.0 and grade <= 2.24:
            num_c_pluses += 1
        else:
            if grade < 2.0:
                num_c_minus += 1
            else:
                num_c_pluses += 1
    
    # determine the number of D+, D, D-, etc.
    num_d_pluses = 0
    num_d_minus = 0
    for grade in grades:
        if grade >= 1.0 and grade <= 1.24:
            num_d_pluses += 1
        else:
            if grade < 1.0:
                num_d_minus += 1
            else:
                num_d_pluses += 1
    
    # determine the number of E
    num_e = len(grades)
    
    # create the list of letter grades
    for
