
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
    grade_equation = {0.0: 'E', 1.0: 'D-', 2.0: 'D', 3.0: 'D+', 4.0: 'C-', 5.0: 'C', 6.0: 'C+', 7.0: 'B-', 8.0: 'B', 9.0: 'B+', 10.0: 'A-', 11.0: 'A', 12.0: 'A+'}
    return list(map(lambda x: grade_equation[x], grades))
    

