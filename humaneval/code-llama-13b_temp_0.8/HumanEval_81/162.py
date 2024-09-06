
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
    # Check the type of grades:
    if not isinstance(grades, list):
        raise TypeError("'grades' must be a list of numbers")

    # Define the letter grades in the proper order:
    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']

    # Find the length of grades:
    length = len(grades)

    # Initialize the list of letter grades:
    letter_grades_list = []

    # Check if grades are in proper range:
    for grade in grades:
        if grade > 4.0 or grade < 0:
            raise ValueError("grade must be in the inclusive range of 0 to 4")

    # Loop through grades list and find the letter grade:
    for grade in grades:
        # For grades equal to 4.0 or greater:
        if grade >= 4.0:
            # Add the grade letter to the list:
            letter_grades_list.append(letter_grades[0])
        # For grades less than 4.0 but greater than 3.7:
        elif grade >= 3.7:
            # Add the grade letter to the list:
            letter_grades_list.append(letter_grades[1])
        # For grades less than 3.7 but greater than 3.3:
        elif grade >= 3.3:
            # Add the grade letter to the list:
            letter_grades_list.append(letter_grades[2])
        # For grades less than 3.3 but greater than 3.0:
        elif grade >= 3.0:
            # Add the grade letter to the list:
            letter_grades_list.append(letter_grades[3])
        # For grades less than 3.0 but greater than 2.7:
        elif grade >= 2.7:
            # Add the grade letter to the list:
            letter_grades_list.append(letter_
