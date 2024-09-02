
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
    # If there are no students or if there are only 2 students, return a list
    # with the 2 students' grades.
    if len(grades) < 2:
        return [grades[0], grades[1]]
    
    # Initialize empty list for the letter grades.
    letter_grades = []
    
    # Get the highest GPA.
    max_gpa = max(grades)
    
    # Get the letter grade for the highest GPA.
    letter_grade = get_letter_grade(max_gpa)
    
    # Find the index of the highest GPA in the list of grades.
    max_index = bisect_left(grades, max_gpa)
    
    # Get the grade before the highest GPA.
    grade_before_max = grades[max_index - 1]
    
    # If the grade before the highest GPA is greater than or equal to 3.0 and
    # less than or equal to 3.3, output the letter grade for 3.3.
    if grade_before_max >= 3.0 and grade_before_max <= 3.3:
        letter_grades.append(get_letter_grade(3.3))
    # If the grade before the highest GPA is greater than or equal to 2.7 and
    # less than or equal to 3.0, output the letter grade for 3.0.
    elif grade_before_max >= 2.7 and grade_before_max <= 3.0:
        letter_grades.append(get_letter_grade(3.0))
    # If the grade before the highest GPA is greater than or equal to 2.3 and
    # less than or equal to 2.7, output the letter grade for 2.7.
    elif grade_before_max >= 2.3 and grade_before_max <= 2.7:
        letter_grades.append(get_letter_grade(2.7))
    # If the grade before the highest GPA is greater than or equal to 2.0 and
    # less than or equal to 2.3, output the letter
