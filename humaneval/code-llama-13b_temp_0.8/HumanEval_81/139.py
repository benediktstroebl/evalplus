
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
    grade = ["E", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"]
    result = []
    for x in grades:
        if x >= 4:
            result.append(grade[0])
        elif x >= 3.7:
            result.append(grade[1])
        elif x >= 3.3:
            result.append(grade[2])
        elif x >= 3:
            result.append(grade[3])
        elif x >= 2.7:
            result.append(grade[4])
        elif x >= 2.3:
            result.append(grade[5])
        elif x >= 2:
            result.append(grade[6])
        elif x >= 1.7:
            result.append(grade[7])
        elif x >= 1.3:
            result.append(grade[8])
        elif x >= 1:
            result.append(grade[9])
        elif x >= 0.7:
            result.append(grade[10])
        elif x >= 0:
            result.append(grade[11])
        else:
            result.append(grade[12])
    return result
