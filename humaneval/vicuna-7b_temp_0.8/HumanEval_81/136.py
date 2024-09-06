
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
    # Loop through the grades
    for grade in grades:
        # Check if the GPA is greater than or equal to 4.0
        if grade >= 4.0:
            # If the GPA is greater than 4.0, output an A+
            letter_grades.append('A+')
        elif grade >= 3.7:
            # If the GPA is greater than or equal to 3.7, output an A
            letter_grades.append('A')
        elif grade >= 3.3:
            # If the GPA is greater than or equal to 3.3, output a B+
            letter_grades.append('B+')
        elif grade >= 3.0:
            # If the GPA is greater than or equal to 3.0, output a B
            letter_grades.append('B')
        elif grade >= 2.7:
            # If the GPA is greater than or equal to 2.7, output a B-
            letter_grades.append('B-')
        elif grade >= 2.3:
            # If the GPA is greater than or equal to 2.3, output a C+
            letter_grades.append('C+')
        elif grade >= 1.7:
            # If the GPA is greater than or equal to 1.7, output a C
            letter_grades.append('C')
        elif grade >= 1.3:
            # If the GPA is greater than or equal to 1.3, output a C-
            letter_grades.append('C-')
        elif grade >= 1.0:
            # If the GPA is greater than or equal to 1.0, output a D+
            letter_grades.append('D+')
        elif grade > 0.7:
            # If the GPA is greater than 0.7, output a D
            letter_grades.append('D')
        elif grade > 0.0:
            # If the GPA is greater than 0.0, output a D-
            letter
