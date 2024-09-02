
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
    grades_dict = {}

    for i in range(0, 10):
        grades_dict[i/10] = 'E'

    grades_dict[4.0] = 'A+'
    grades_dict[3.7] = 'A'
    grades_dict[3.3] = 'A-'
    grades_dict[3.0] = 'B+'
    grades_dict[2.7] = 'B'
    grades_dict[2.3] = 'B-'
    grades_dict[2.0] = 'C+'
    grades_dict[1.7] = 'C'
    grades_dict[1.3] = 'C-'
    grades_dict[1.0] = 'D+'
    grades_dict[0.7] = 'D'
    grades_dict[0.0] = 'D-'

    return [grades_dict.get(grade) for grade in grades]

