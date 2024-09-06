
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
    gpagrades = []
    for course_gpa in grades:
        if course_gpa >= 4.0:
            gpagrades.append("A+")
        elif course_gpa >= 3.7:
            gpagrades.append("A")
        elif course_gpa >= 3.3:
            gpagrades.append("A-")
        elif course_gpa >= 3.0:
            gpagrades.append("B+")
        elif course_gpa >= 2.7:
            gpagrades.append("B")
        elif course_gpa >= 2.3:
            gpagrades.append("B-")
        elif course_gpa >= 2.0:
            gpagrades.append("C+")
        elif course_gpa >= 1.7:
            gpagrades.append("C")
        elif course_gpa >= 1.3:
            gpagrades.append("C-")
        elif course_gpa >= 1.0:
            gpagrades.append("D+")
        elif course_gpa >= 0.7:
            gpagrades.append("D")
        elif course_gpa >= 0.0:
            gpagrades.append("D-")
        else:
            gpagrades.append("E")
    return gpagrades
            


grades = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
