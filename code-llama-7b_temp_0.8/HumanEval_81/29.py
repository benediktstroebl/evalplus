
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
    if not grades:
        return []

    grades = [str(grade) for grade in grades]
    grade_points = [float(grade) for grade in grades]

    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    letter_grades_point = [4.0, 4.0, 4.0, 3.7, 3.7, 3.7, 3.3, 3.3, 3.3, 2.7, 2.7, 2.7, 0]

    grade_dict = {}

    for idx, letter_grade in enumerate(letter_grades):
        grade_dict[letter_grade] = letter_grades_point[idx]

    final_grades = []

    for grade_point in grade_points:
        for letter_grade, gpa in grade_dict.items():
            if gpa <= grade_point:
                final_grades.append(letter_grade)
                break

    return final_grades
