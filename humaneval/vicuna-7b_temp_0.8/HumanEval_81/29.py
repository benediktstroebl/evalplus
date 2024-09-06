
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
    # Check if there is a single grade in the list
    if len(grades) == 1:
        return [grades[0]]

    # Initialize the final grades list
    final_grades = []

    # Iterate over the list of GPAs and add each one to the final list
    for gpa in grades:
        # If the GPA is less than or equal to 3.0, add the GPA to the list
        if gpa <= 3.0:
            final_grades.append(gpa)
        # If the GPA is greater than 3.0, check if it is greater than or equal to 3.7
        else:
            if gpa >= 3.7:
                final_grades.append('A')
            elif gpa >= 3.3:
                final_grades.append('A-')
            elif gpa >= 3.0:
                final_grades.append('B')
            elif gpa >= 2.7:
                final_grades.append('B-')
            elif gpa >= 2.3:
                final_grades.append('C')
            elif gpa >= 1.7:
                final_grades.append('C-')
            elif gpa >= 1.3:
                final_grades.append('D')
            elif gpa >= 0.7:
                final_grades.append('D+')
            elif gpa >= 0.0:
                final_grades.append('E')
            else:
                final_grades.append('F')
    return final_grades
