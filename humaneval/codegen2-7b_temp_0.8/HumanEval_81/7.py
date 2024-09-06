
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
    grade_list = []
    for grade in grades:
        if grade >= 4.0 and grade < 4.5:
            grade_list.append("A+")
        elif grade >= 4.5 and grade < 5.0:
            grade_list.append("A")
        elif grade >= 5.0 and grade < 5.5:
            grade_list.append("A-")
        elif grade >= 5.5 and grade < 6.0:
            grade_list.append("B+")
        elif grade >= 6.0 and grade < 6.5:
            grade_list.append("B")
        elif grade >= 6.5 and grade < 7.0:
            grade_list.append("B-")
        elif grade >= 7.0 and grade < 8.0:
            grade_list.append("C+")
        elif grade >= 8.0 and grade <= 8.5:
            grade_list.append("C")
        elif grade >= 8.5:
            grade_list.append("C-")
    return
