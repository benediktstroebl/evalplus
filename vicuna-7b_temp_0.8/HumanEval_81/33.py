
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

    # Check if the list of grades is empty
    if not grades:
        return []

    # Initialize a list to store the letter grades
    letter_grades = []

    # Calculate the GPA of each student
    for grade in grades:
        gpa = calculate_gpa(grade)
        letter_grades.append(str(gpa))

    # Sort the list of grades in descending order
    sorted_grades = sorted(letter_grades, reverse=True)

    # Initialize an empty list to store the letter grades
    letter_grades_output = []

    # Loop through the sorted list of grades
    for grade in sorted_grades:
        # Check if the grade is greater than 3.0
        if grade >= 3.0:
            # Check if the grade is greater than 3.3
            if grade >= 3.3:
                # Check if the grade is greater than 3.7
                if grade >= 3.7:
                    # Output a plus for the letter grade
                    letter_grades_output.append('+')
                else:
                    # Output an A for the letter grade
                    letter_grades_output.append('A')
            else:
                # Output an A- for the letter grade
                letter_grades_output.append('A-')
        else:
            # Check if the grade is greater than 2.3
            if grade >= 2.3:
                # Output a B for the letter grade
                letter_grades_output.append('B')
            else:
                # Output a C for the letter grade
                letter_grades_output.append('C')
        else:
            # Output a D for the letter grade
            letter_grades_output.append('D')

    # Sort the list of letter grades in descending order
    sorted_letter_grades = sorted(letter_grades_output, reverse=True)

    return sorted_letter_grades
