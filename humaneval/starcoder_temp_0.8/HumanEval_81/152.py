
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
    # write your answer between #start and #end
    #start
    a = grades[0]
    if a >= 4.0:
        a = "A+"
    elif a >= 3.7:
        a = "A"
    elif a >= 3.3:
        a = "A-"
    elif a >= 3.0:
        a = "B+"
    elif a >= 2.7:
        a = "B"
    elif a >= 2.3:
        a = "B-"
    elif a >= 2.0:
        a = "C+"
    elif a >= 1.7:
        a = "C"
    elif a >= 1.3:
        a = "C-"
    elif a >= 1.0:
        a = "D+"
    elif a >= 0.7:
        a = "D"
    elif a >= 0.0:
        a = "D-"
    else:
        a = "E"

    b = grades[1]
    if b >= 4.0:
        b = "A+"
    elif b >= 3.7:
        b = "A"
    elif b >= 3.3:
        b = "A-"
    elif b >= 3.0:
        b = "B+"
    elif b >= 2.7:
        b = "B"
    elif b >= 2.3:
        b = "B-"
    elif b >= 2.0:
        b = "C+"
    elif b >= 1.7:
        b = "C"
    elif b >= 1.3:
        b = "C-"
    elif b >= 1.0:
        b = "D+"
    elif b >= 0.7:
        b = "D"
    elif b >= 0.0:
        b = "D-"
    else:
        b = "E"

    c = grades[2]
    if c >= 4.0:
        c = "A+"
    elif c >= 3.7:
        c = "A"
    elif c >= 3.3:
        c = "A-"
    elif c >= 3.0:
        c = "B+"
    elif c >= 2.7:
        c = "B"
    elif c >= 2.3:
        c = "B-"
    elif c >= 2
