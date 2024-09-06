
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
    letter_grade_grade = ['' for _ in range(len(grades))]
    second_grade_grade = []
    grades = sorted(grades)
    for i in range(len(grades)):
        if grades[i] > 3.7:
            second_grade_grade.append('A')
        elif grades[i] > 3.3:
            second_grade_grade.append('A-')
        elif grades[i] > 3.0:
            second_grade_grade.append('B')
        elif grades[i] > 2.7:
            second_grade_grade.append('B-')
        elif grades[i] > 2.3:
            second_grade_grade.append('C')
        elif grades[i] > 2.0:
            second_grade_grade.append('C-')
        elif grades[i] > 1.7:
            second_grade_grade.append('D')
        elif grades[i] > 1.3:
            second_grade_grade.append('D-')
        elif grades[i] > 1.0:
            second_grade_grade.append('E')
        elif grades[i] > 0.7:
            second_grade_grade.append('D-')
        elif grades[i] > 0.0:
            second_grade_grade.append('F')
    grades = [grades[i] for i in range(len(grades)) if grades[i] <= 0]
    grades = [grades[i] for i in range(len(grades)) if grades[i] >= 0]
    grades = [grades[i] for i in range(len(grades)) if grades[i] == 0]
    if len(grades) != 0:
        for i in range(len(grades)):
            if grades[i] >= 4.0:
                letter_grade_grade[i] = 'A+'
            elif grades[i] >= 3.7:
                letter_grade_grade[i] = 'A'
            elif grades[i] >= 3.3:
                letter_grade_grade[i] = 'A-'
            elif