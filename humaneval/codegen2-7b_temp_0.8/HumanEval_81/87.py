
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
    output = []
    for grade in grades:
        if grade < 4:
            output.append("A+")
        elif grade > 4 and grade < 3.8:
            output.append("A")
        elif grade > 3.8 and grade < 3.3:
            output.append("A-")
        elif grade > 3.3 and grade < 2.8:
            output.append("B+")
        elif grade > 2.8 and grade < 2.3:
            output.append("B")
        elif grade > 2.3 and grade < 1.8:
            output.append("B-")
        elif grade > 1.8 and grade < 1.3:
            output.append("C+")
        elif grade > 1.3 and grade < 0.8:
            output.append("C")
        else:
            output.append("D")
    
