
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
    # Check if the list of GPAs is empty or not
    if not grades:
        return []
    
    # Sort the list of GPAs in ascending order
    grades = sorted(grades)
    
    # Initialize an empty list to store the letter grades
    letter_grades = []
    
    # Loop through the sorted list of GPAs
    for grade in grades:
        # Check if the GPA is greater than 3.7
        if grade > 3.7:
            # If the GPA is greater than 3.7, the letter grade is A
            letter_grades.append('A')
        # Check if the GPA is greater than 3.3 and less than 3.7
        elif grade > 3.3 and grade < 3.7:
            # If the GPA is greater than 3.3 and less than 3.7, the letter grade is A-
            letter_grades.append('A-')
        # Check if the GPA is greater than 3.0 and less than 3.3
        elif grade > 3.0 and grade < 3.3:
            # If the GPA is greater than 3.0 and less than 3.3, the letter grade is B+
            letter_grades.append('B+')
        # Check if the GPA is greater than 2.7 and less than 3.0
        elif grade > 2.7 and grade < 3.0:
            # If the GPA is greater than 2.7 and less than 3.0, the letter grade is B
            letter_grades.append('B')
        # Check if the GPA is greater than 2.3 and less than 2.7
        elif grade > 2.3 and grade < 2.7:
            # If the GPA is greater than 2.3 and less than 2.7, the letter grade is B-
            letter_grades.append('B-')
        # Check if the GPA is greater than 2.0 and less than 2.3
        elif grade > 2.0 and grade < 2.3:
            # If the GPA is greater than
