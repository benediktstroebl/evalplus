
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
    
    # Iterate over the list of GPAs
    for gpa in grades:
        # Check if the gpa is less than 3.0
        if gpa < 3.0:
            # If it is, then add 'D-' to the list of letter grades
            letter_grades.append('D-')
        elif gpa < 2.7:
            # If it is not, then check if the next gpa is greater than or equal to 3.0
            if (gpa + 0.3) >= 3.0:
                # If it is, then add 'D' to the list of letter grades
                letter_grades.append('D')
            else:
                # If it is not, then add 'D-' to the list of letter grades
                letter_grades.append('D-')
        else:
            # If it is greater than 3.0, then check if it is greater than or equal to 3.7
            if (gpa + 0.3) >= 3.7:
                # If it is, then add 'A' to the list of letter grades
                letter_grades.append('A')
            elif (gpa + 0.3) >= 3.3:
                # If it is not, then check if the next gpa is greater than or equal to 3.7
                if (gpa + 0.3) >= 3.3:
                    # If it is, then add 'A-' to the list of letter grades
                    letter_grades.append('A-')
                else:
                    # If it is not, then add 'B' to the list of letter grades
                    letter_grades.append('B')
            else:
                # If it is not, then add 'B-' to the list of letter grades
                letter_grades.append('B-')
    return letter_grades
