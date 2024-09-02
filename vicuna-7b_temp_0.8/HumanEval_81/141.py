
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
    # Check if the list is empty
    if not grades:
        return []

    # Initialize the output list
    grades_list = []

    # Check if the first element is greater than 3.7
    if grades[0] > 3.7:
        grade = grades[0]
    else:
        # Check if the next elements are greater than 3.3 and grades[1] > 2.7
        if (grades[1] > 3.3 and grades[2] > 2.7) or (grades[1] > 2.7 and grades[2] > 3.3):
            grade = 3.0
        else:
            grade = 2.0
    
    # Check if the next elements are greater than 2.7 and grades[3] > 1.7
    if (grades[2] > 2.7 and grades[3] > 1.7) or (grades[2] > 1.7 and grades[3] > 2.7):
        grade += 0.3
    else:
        grade += 0.0
    
    # Check if the next elements are greater than 1.7 and grades[4] > 0.7
    if (grades[3] > 1.7 and grades[4] > 0.7) or (grades[3] > 0.7 and grades[4] > 1.7):
        grade += 0.3
    else:
        grade += 0.0
    
    # Append the grade to the output list
    grades_list.append(str(grade))
    
    # Check if there is another element in the list
    if grades:
        # Update the grade by multiplying by 1.05
        grade *= 1.05
        # Repeat the process
        grades_list.extend(numerical_letter_grade(grades_list))
    
    return grades_list
