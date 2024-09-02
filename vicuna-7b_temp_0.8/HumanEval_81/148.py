
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
    # Initialize a dictionary with the letter grade as keys and None as values
    letter_grade = {4.0 : 'A+',
                    3.7 : 'A',
                    3.3 : 'A-',
                    3.0 : 'B+',
                    2.7 : 'B',
                    2.3 : 'B-',
                    2.0 : 'C+',
                    1.7 : 'C',
                    1.3 : 'C-',
                    1.0 : 'D+',
                    0.7 : 'D',
                    0.0 : 'D-',
                    0.0 : 'E'}

    # Iterate over the list of GPAs and check if the current GPA is greater than 3.0
    for grade in grades:
        if grade > 3.0:
            # If the current GPA is greater than 3.0, check what letter grade to assign
            letter_grade[grade] = None

    # If the last GPA is less than or equal to 3.0, assign it an F
    for i in range(len(grades)-1, -1, -1):
        if grades[i] <= 3.0:
            letter_grade[grades[i]] = 'F'

    return letter_grade.values()