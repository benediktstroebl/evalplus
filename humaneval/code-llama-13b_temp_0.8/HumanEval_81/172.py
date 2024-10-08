
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
    gradelist = []
    for x in grades:
        if x == 0:
            gradelist.append("E")
        if x > 0 and x < 1:
            gradelist.append("D-")
        if x >= 1 and x <= 1.3:
            gradelist.append("D")
        if x > 1.3 and x <= 1.7:
            gradelist.append("D+")
        if x > 1.7 and x <= 2:
            gradelist.append("C-")
        if x > 2 and x <= 2.3:
            gradelist.append("C")
        if x > 2.3 and x <= 2.7:
            gradelist.append("C+")
        if x > 2.7 and x <= 3:
            gradelist.append("B-")
        if x > 3 and x <= 3.3:
            gradelist.append("B")
        if x > 3.3 and x <= 3.7:
            gradelist.append("B+")
        if x > 3.7 and x <= 4:
            gradelist.append("A-")
        if x > 4:
            gradelist.append("A")
    return gradelist
