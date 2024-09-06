
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

    # Define the letter grades
    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-']
    letter_grades.reverse()

    # Define a list for the output
    output = []

    # Loop through the list of grades
    for grade in grades:

        # Create a variable for the index of the grade
        index = 0

        # Loop through the letter grades
        for letter_grade in letter_grades:

            # If the grade is greater than the current letter grade
            if grade >= letter_grades[index]:

                # Add the letter grade to the output list
                output.append(letter_grade)

                # Break from the loop
                break

            # Increase the index
            index += 1

    # Return the output list
    return output
