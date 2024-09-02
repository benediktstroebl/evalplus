
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

    if not isinstance(grades, list):
        return 'Error! The input must be a list of numbers'

    if len(grades) == 0:
        return 'Error! List is empty'

    grades = sorted(grades)

    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']

    for i, val in enumerate(grades):
        if val >= 4.0:
            grades[i] = letters[0]
            del letters[0]
            continue
        if val >= 3.7:
            grades[i] = letters[1]
            del letters[1]
            continue
        if val >= 3.3:
            grades[i] = letters[2]
            del letters[2]
            continue
        if val >= 3.0:
            grades[i] = letters[3]
            del letters[3]
            continue
        if val >= 2.7:
            grades[i] = letters[4]
            del letters[4]
            continue
        if val >= 2.3:
            grades[i] = letters[5]
            del letters[5]
            continue
        if val >= 2.0:
            grades[i] = letters[6]
            del letters[6]
            continue
        if val >= 1.7:
            grades[i] = letters[7]
            del letters[7]
            continue
        if val >= 1.3:
            grades[i] = letters[8]
            del letters[8]
            continue
        if val >= 1.0:
            grades[i] = letters[9]
            del letters[9]
            continue
        if val >= 0.7:
            grades[i] = letters[10]
            del letters[10]
            continue
        if val >= 0.0:
            grades[i] = letters[11]
            del letters[11]
            continue
        grades[i] = letters[12]
        del letters[12]

    return grades
