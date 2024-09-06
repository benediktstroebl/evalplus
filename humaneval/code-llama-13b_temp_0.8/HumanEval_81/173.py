
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
    
    a_plus = []
    a = []
    a_minus = []
    b_plus = []
    b = []
    b_minus = []
    c_plus = []
    c = []
    c_minus = []
    d_plus = []
    d = []
    d_minus = []
    e = []
    
    for i in range(len(grades)):
        if grades[i] == 4.0:
            a_plus.append("A+")
        elif 3.7 <= grades[i] <= 4:
            a.append("A")
        elif 3.3 <= grades[i] <= 3.69:
            a_minus.append("A-")
        elif 3.0 <= grades[i] <= 3.29:
            b_plus.append("B+")
        elif 2.7 <= grades[i] <= 2.99:
            b.append("B")
        elif 2.3 <= grades[i] <= 2.69:
            b_minus.append("B-")
        elif 2.0 <= grades[i] <= 2.29:
            c_plus.append("C+")
        elif 1.7 <= grades[i] <= 1.99:
            c.append("C")
        elif 1.3 <= grades[i] <= 1.69:
            c_minus.append("C-")
        elif 1.0 <= grades[i] <= 1.29:
            d_plus.append("D+")
        elif 0.7 <= grades[i] <= 0.99:
            d.append("D")
        elif 0.0 <= grades[i] <= 0.69:
            d_minus.append("D-")
        elif grades[i] == 0.0:
            e.append("E")
        else:
            raise Exception("Invalid score - it should be between 0.0 and 4.0")
    return a_plus + a + a_minus + b_plus +
