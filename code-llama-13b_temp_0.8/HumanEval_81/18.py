
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

    # The table with letter grades
    letter_grades = [
        ['A+', 4.0],
        ['A', 3.7],
        ['A-', 3.3],
        ['B+', 3.0],
        ['B', 2.7],
        ['B-', 2.3],
        ['C+', 2.0],
        ['C', 1.7],
        ['C-', 1.3],
        ['D+', 1.0],
        ['D', 0.7],
        ['D-', 0.3],
        ['E', 0.0]
    ]

    # The letter grade list that will be returned
    letter_grade_list = []

    # Check if there are any grades in the list
    if len(grades) > 0:
        # For every grade in the list
        for grade in grades:
            # Iterate through the list
            for letter_grade in letter_grades:
                # If the grade is greater than or equal to the current letter grade
                if grade >= letter_grade[1]:
                    # Append the letter grade to the letter grade list
                    letter_grade_list.append(letter_grade[0])

                    # Break the loop
                    break

        # Return the letter grade list
        return letter_grade_list

    # If there are no grades in the list
    else:
        # Return the empty list
        return letter_grade_list

