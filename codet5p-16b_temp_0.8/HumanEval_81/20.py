
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

    assert isinstance(grades, list), "Input must be a list of GPA's."
    assert all([isinstance(x, (float, int)) for x in grades]), "All values must be floats."
    assert len(grades) > 0, "Input must have at least one GPA."

    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    for i in range(len(grades)):
        if grades[i] == 4.0:
            grades[i] = letter_grades[0]
        elif grades[i] >= 3.7:
            grades[i] = letter_grades[1]
        elif grades[i] >= 3.3:
            grades[i] = letter_grades[2]
        elif grades[i] >= 3.0:
            grades[i] = letter_grades[3]
        elif grades[i] >= 2.7:
            grades[i] = letter_grades
