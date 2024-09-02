
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
    grades = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    grades = [5.0, 4.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
    grade_points = {
                    'A': 4.0,
                    'A-': 3.7,
                    'B+': 3.3,
                    'B': 3.0,
                    'B-': 2.7,
                    'C+': 2.3,
                    'C': 2.0,
                    'C-': 1.7,
                    'D+': 1.3,
                    'D': 1.0,
                    'D-': 0.7,
                    'E': 0.0
                    }
    grades_equation = []
    for grade in grades:
        if grade >= 4.0:
            letter_grade = "A+"
        elif grade >= 3.7:
            letter_grade = "A"
        elif grade >= 3.3:
            letter_grade = "A-"
        elif grade >= 3.0:
            letter_grade = "B+"
        elif grade >= 2.7:
            letter_grade = "B"
        elif grade >= 2.3:
            letter_grade = "B-"
        elif grade >= 2.0:
            letter_grade = "C+"
        elif grade >= 1.7:
            letter_grade = "C"
        elif grade >= 1.3:
            letter_grade = "C-"
        elif grade >= 1.0:
            letter_grade = "D+"
        elif grade >= 0.7:
            letter_grade = "D"
        elif grade >= 0.0:
            letter_grade = "D-"
        else:
            letter_grade = "E"
        grades_equation.append(letter_grade)
    return grades_equation
