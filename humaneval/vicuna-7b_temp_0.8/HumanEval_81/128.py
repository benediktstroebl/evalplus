
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

    # Loop through the list of GPAs
    for gpa in grades:
        # Check if the GPA is below 3.0
        if gpa < 3.0:
            # If it is, add "D-" to the list of letter grades
            letter_grades.append("D-")
        # Check if the GPA is above 3.7
        elif gpa > 3.7:
            # If it is, add "A" to the list of letter grades
            letter_grades.append("A")
        # Check if the GPA is above 3.3
        elif gpa > 3.3:
            # If it is, add "A-" to the list of letter grades
            letter_grades.append("A-")
        # Check if the GPA is above 3.0
        elif gpa > 3.0:
            # If it is, add "B+" to the list of letter grades
            letter_grades.append("B+")
        # Check if the GPA is above 2.7
        elif gpa > 2.7:
            # If it is, add "B" to the list of letter grades
            letter_grades.append("B")
        # Check if the GPA is above 2.3
        elif gpa > 2.3:
            # If it is, add "B-" to the list of letter grades
            letter_grades.append("B-")
        # Check if the GPA is above 2.0
        elif gpa > 2.0:
            # If it is, add "C+" to the list of letter grades
            letter_grades.append("C+")
        # Check if the GPA is above 1.7
        elif gpa > 1.7:
            # If it is, add "C" to the list of letter grades
            letter_grades.append("C")
        # Check if the GPA is above 1.3
        elif gpa > 1.3:
            # If it is
