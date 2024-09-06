
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

    # empty list to store letter grades
    letter_grades = []
    
    # loop through the list of GPAs
    for gpa in grades:
        # check if the GPA is less than or equal to 3.0
        if gpa <= 3.0:
            # if the GPA is less than 2.0, output a D- grade
            if gpa <= 1.0:
                letter_grades.append('D-')
            else:
                letter_grades.append('D')
        # check if the GPA is greater than 3.0
        elif gpa > 3.0:
            # check if the GPA is greater than 3.7
            if gpa > 3.7:
                letter_grades.append('A')
            # check if the GPA is greater than 3.3 and less than 3.7
            elif gpa > 3.3 and gpa <= 3.7:
                letter_grades.append('A-')
            # check if the GPA is greater than 3.0 and less than 3.3
            elif gpa > 3.0 and gpa <= 3.3:
                letter_grades.append('B')
            # check if the GPA is greater than 2.7 and less than 3.0
            elif gpa > 2.7 and gpa <= 3.0:
                letter_grades.append('B-')
            # check if the GPA is greater than 2.0 and less than 2.7
            elif gpa > 2.0 and gpa <= 2.7:
                letter_grades.append('C')
            # check if the GPA is greater than 1.7 and less than 2.0
            elif gpa > 1.7 and gpa <= 1.9:
                letter_grades.append('C+')
            # check if the GPA is greater than 1.3 and less than 1.7
            elif gpa > 1.3 and gpa <= 1.6:
                letter_grades.append('C-')
            # check if the G
