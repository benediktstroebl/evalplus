
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
    # TODO: Write your function here

    # if 4.0 <= grades <= 4.3:
    #     return "A+"
    # elif 3.7 <= grades <= 4.0:
    #     return "A"
    # elif 3.3 <= grades <= 3.7:
    #     return "A-"
    # elif 3.0 <= grades <= 3.3:
    #     return "B+"
    # elif 2.7 <= grades <= 3.0:
    #     return "B"
    # elif 2.3 <= grades <= 2.7:
    #     return "B-"
    # elif 2.0 <= grades <= 2.3:
    #     return "C+"
    # elif 1.7 <= grades <= 2.0:
    #     return "C"
    # elif 1.3 <= grades <= 1.7:
    #     return "C-"
    # elif 1.0 <= grades <= 1.3:
    #     return "D+"
    # elif 0.7 <= grades <= 1.0:
    #     return "D"
    # elif 0.0 <= grades <= 0.7:
    #     return "D-"
    # else:
    #     return "E"
    res = []
    for grade in grades:
        if grade >= 4:
            res.append("A+")
        elif grade >= 3.7:
            res.append("A")
        elif grade >= 3.3:
            res.append("A-")
        elif grade >= 3:
            res.append("B+")
        elif grade >= 2.7:
            res.append("B")
        elif grade >= 2.3:
            res.append("B-")
        elif grade >= 2:
            res.append("C+")
        elif grade >= 1.7:
            res.append("C")
        elif grade >= 1.3:
            res.append("C-")
        elif grade >= 1:
            res
