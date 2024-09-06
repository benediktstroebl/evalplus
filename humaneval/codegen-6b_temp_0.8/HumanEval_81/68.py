
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
    def grade_compare(grade1, grade2):
        if grade1 > grade2:
            return 1
        elif grade1 < grade2:
            return -1
        else:
            return 0

    grades.sort(reverse=True, key=lambda x:x[0])
    grade_grades = [grade for (grade, student) in grades]
    letter_grades = [grade[1] for grade in grades]

    for index, letter_grade in enumerate(letter_grades):
        letter_grades[index] = letter_grade.lower()

    for position in range(len(grades)):
        if grade_grades[position] == 4.0:
            letter_grades[position] = 'A+'

        elif grade_grades[position] > 3.7:
            letter_grades[position] = 'A'

        elif grade_grades[position] > 3.3:
            letter_grades[position] = 'A-'

        elif grade_grades[position] > 3.0:
            letter_grades[position] = 'B+'

        elif grade_grades[position] > 2.7:
            letter_grades[position] = 'B'

        elif grade_grades[position] > 2.3:
            letter_grades[position] = 'B-'

        elif grade_grades[position] > 2.0:
            letter_grades[position] = 'C+'

        elif grade_grades[position] > 1.7:
            letter_grades[position] = 'C'

        elif grade_grades[position] > 1.3:
            letter_grades[position] = 'C-'

        elif grade_grades[position] > 1.0:
            letter_grades[position] = 'D+'

        elif grade_grades[position] > 0.7:
            letter_grades[position] = 'D'

        elif grade_grades[position] > 0.0:
            letter_grades[position] = 'D-'

    return letter_grades
