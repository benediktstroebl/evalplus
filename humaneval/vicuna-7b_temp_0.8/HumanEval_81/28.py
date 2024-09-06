
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
    # creating a dictionary to store the letter grades for each GPA
    letter_grades = {
        '4.0': 'A+',
        '3.7': 'A',
        '3.3': 'A-',
        '3.0': 'B+',
        '2.7': 'B',
        '2.3': 'B-',
        '2.0': 'C+',
        '1.7': 'C',
        '1.3': 'C-',
        '1.0': 'D+',
        '0.7': 'D',
        '0.0': 'D-',
        '0.0': 'E'
    }
    
    # looping through the list of GPAs
    for gpa in grades:
        # if the GPA is less than or equal to 3.0, it should get a letter grade of B+ or lower
        if gpa <= 3.0:
            letter_grade = 'B'
            if gpa >= 2.7:
                letter_grade = 'B+'
            elif gpa >= 2.3:
                letter_grade = 'B'
            elif gpa >= 2.0:
                letter_grade = 'C+'
            elif gpa >= 1.7:
                letter_grade = 'C'
            elif gpa >= 1.3:
                letter_grade = 'C-'
            elif gpa >= 1.0:
                letter_grade = 'D+'
            else:
                letter_grade = 'D'
            break
        # if the GPA is greater than 3.0 but less than 3.7, it should get a letter grade of A-
        elif gpa > 3.0 and gpa <= 3.7:
            letter_grade = 'A-'
            break
        # if the GPA is greater than 3.7, it should get an A
        elif gpa > 3.7:
            letter_grade = 'A'
            break
        # if the GPA is greater than 4.0, it should get an A+
        elif gpa > 4.0:
            letter
