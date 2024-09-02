
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
    letter_grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'D', 'E']
    midpoint = sum(grades) / len(grades)
    grades_sorted = sorted(grades, reverse=True)
    average = sum(grades_sorted) / len(grades_sorted)
    grades_grade_boundary = [2.66666667, 2.33333333, 2.0, 1.66666667, 1.33333333, 1.0, 0.66666667, 0.0]
    
    for grade in grades_sorted:
        if grade < midpoint:
            letter_grade = letter_grade[0]
        elif average < grade_grade_boundary[0]:
            letter_grade = letter_grade[1]
        elif average < grade_grade_boundary[1]:
            letter_grade = letter_grade[2]
        elif average < grade_grade_boundary[2]:
            letter_grade = letter_grade[3]
        elif average < grade_grade_boundary[3]:
            letter_grade = letter_grade[4]
        elif average < grade_grade_boundary[4]:
            letter_grade = letter_grade[5]
        elif average < grade_grade_boundary[5]:
            letter_grade = letter_grade[6]
        elif average < grade_grade_boundary[6]:
            letter_grade = letter_grade[7]
        elif average < grade_grade_boundary[7]:
            letter_grade = letter_grade[8]
        else:
            letter_grade = letter_grade[9]
    
    return letter_grade