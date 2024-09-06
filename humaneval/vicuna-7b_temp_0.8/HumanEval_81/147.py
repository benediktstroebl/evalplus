
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
    letter_grades = []
    average = sum(grades) / len(grades)
    for grade, gpa in grades:
        if gpa < 0:
            return []
        if average - gpa < 0.5:
            return []
        if average - gpa > 3.6:
            return [None]
        if average - gpa < 0.2 and average - gpa > 0.1:
            return [None]
        if gpa < 2.6:
            return [None]
        if average - gpa < 0.4:
            return [None]
        if average - gpa > 2.8:
            return [None]
        if average - gpa < 0.6 and average - gpa > 0.5:
            return [None]
        if average - gpa < 0.2 and average - gpa > 0.1:
            return [None]
        if average - gpa > 2.8:
            return [None]
        if average - gpa < 0.4:
            return [None]
        if average - gpa > 0.6:
            return [None]
        if average - gpa < 0.2:
            return [None]
        if average - gpa > 0.1:
            return [None]
        if average - gpa < 0.4:
            return [None]
        if average - gpa > 0.6:
            return [None]
        if average - gpa < 0.2:
            return [None]
        if average - gpa > 0.1:
            return [None]
        if average - gpa < 0.4:
            return [None]
        if average - gpa > 0.6:
            return [None]
        if average - gpa < 0.2:
            return [None]
        if average - gpa > 0.1:
            return [None]
        if average - gpa < 0.4:
            return [None]
        if average - gpa > 0.6:
            return [None]
    return
