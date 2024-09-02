
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
    a = 4.0
    b = 3.7
    c = 3.3
    d = 3.0
    e = 2.7
    f = 2.3
    g = 2.0
    h = 1.7
    i = 1.3
    j = 1.0
    k = 0.7
    l = 0.0
    z = 0.0

    result = []
    for gpa in grades:
        if gpa >= a:
            result.append("A+")
        elif a > gpa > b:
            result.append("A")
        elif b > gpa > c:
            result.append("A-")
        elif c > gpa > d:
            result.append("B+")
        elif d > gpa > e:
            result.append("B")
        elif e > gpa > f:
            result.append("B-")
        elif f > gpa > g:
            result.append("C+")
        elif g > gpa > h:
            result.append("C")
        elif h > gpa > i:
            result.append("C-")
        elif i > gpa > j:
            result.append("D+")
        elif j > gpa > k:
            result.append("D")
        elif k > gpa > l:
            result.append("D-")
        else:
            result.append("E")
    return result
