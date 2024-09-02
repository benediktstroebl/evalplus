
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
    # Create an empty list to store the letter grades
    letter_grades = []
    
    # Loop through the grades and calculate the GPA
    for grade in grades:
        # If the grade is missing, use 0.0 as a placeholder
        if grade is None:
            letter_grades.append(0.0)
        else:
            letter_grades.append(grade)
    
    # Calculate the GPA
    total = sum(letter_grades)
    total = (total / len(letter_grades)) if len(letter_grades) > 0 else 0.0
    
    # Calculate the number of A's
    num_a = 0
    for grade in letter_grades:
        if grade > 3.7:
            num_a += 1
        elif grade > 3.3:
            num_a += 1
        elif grade > 3.0:
            num_a += 1
    
    # Calculate the number of A+'s
    num_a_plus = 0
    for grade in letter_grades:
        if grade > 4.0:
            num_a_plus += 1
    
    # Calculate the number of B's
    num_b = 0
    for grade in letter_grades:
        if grade > 2.7:
            num_b += 1
        elif grade > 2.3:
            num_b += 1
    
    # Calculate the number of B+'s
    num_b_plus = 0
    for grade in letter_grades:
        if grade > 2.7 and num_b == 0:
            num_b_plus += 1
        elif grade > 2.3 and num_b == 1:
            num_b_plus += 1
    
    # Calculate the number of C's
    num_c = 0
    for grade in letter_grades:
        if grade > 1.7:
            num_c += 1
        elif grade > 1.3:
            num_c += 1
    
    #
