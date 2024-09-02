
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
    # Create a list to store the letter grades
    letter_grades = []
    # Check if the list is empty
    if not grades:
        return letter_grades
    # Iterate through the list of grades
    for grade in grades:
        # Check if the grade is greater than or equal to 3.0
        if grade >= 3.0:
            # Check if the grade is greater than the next highest grade
            if letter_grades[-1] not in [grade, grade+1]:
                # Append the grade to the list of letter grades
                letter_grades.append(grade)
        else:
            # Append the highest grade in the list to the list of letter grades
            letter_grades.append(max(letter_grades))
    return letter_grades
