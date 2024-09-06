
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
    grades_list = [None, 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']
    letter_grades = [None, 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+']
    for i in range(1, len(grades_list)):
        grades_list[i] = (letter_grades[i-1], grades_list[i-1])
    # for index, grade in enumerate(grades):
    #     for letter_grade in range(len(grades_list)):
    #         if grades[index] >= grades_list[letter_grade][1]:
    #             grades[index] = grades_list[letter_grade][0]
    #             break

    return [grades_list[letter_grades.index(grades_list.index(grade))][0] for grade in grades]
