
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
    # Create a dictionary to store the letter grades
    letter_grades = {}

    # Loop through the list of GPAs
    for gpa in grades:
        # Check if the GPA is greater than or equal to 4.0
        if gpa >= 4.0:
            # Look up the corresponding letter grade in the dictionary
            letter_grade = letter_grades.get(gpa)
            if letter_grade is None:
                # If the letter grade is not found, it means the GPA is not 
                # in the dictionary, so the letter grade is 'A+'
                letter_grade = 'A+'
            else:
                # If the letter grade is found, increment the count of that letter
                letter_grade_count = letter_grades.get(letter_grade, 0) + 1
                letter_grades[letter_grade] = letter_grade_count

    # Sort the letter grades by their count
    letter_grades = sorted(letter_grades.items(), key=lambda x: x[1], reverse=True)

    # Create a list of letter grades
    return list(letter_grades.values())
