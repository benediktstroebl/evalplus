
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
    for gpa in grades:
        if gpa < 0.0:
            letter_grades.append(f"{gpa:.2f} E")
        elif 0.0 <= gpa <= 1.749:
            letter_grades.append("D-")
        elif 1.75 <= gpa <= 2.000:
            letter_grades.append("D")
        elif 2.000 <= gpa <= 2.249:
            letter_grades.append("D+")
        elif 2.25 <= gpa <= 2.499:
            letter_grades.append("C-")
        elif 2.500 <= gpa <= 2.649:
            letter_grades.append("C")
        elif 2.650 <= gpa <= 2.749:
            letter_grades.append("C+")
        elif 2.750 <= gpa <= 3.000:
            letter_grades.append("B-")
        elif 3.000 <= gpa <= 3.249:
            letter_grades.append("B")
        elif 3.250 <= gpa <= 3.399:
            letter_grades.append("B+")
        elif 3.400 <= gpa <= 3.599:
            letter_grades.append("A-")
        elif 3.600 <= gpa <= 3.749:
            letter_grades.append("A")
        elif 3.750 <= gpa <= 3.899:
            letter_grades.append("A+")
        else:
            letter_grades.append("A+")
    return letter_grades
