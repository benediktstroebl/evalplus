
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

    grade_table = {
        "A+": (4.0, 100),
        "A": (3.7, 93),
        "A-": (3.3, 86),
        "B+": (3.0, 80),
        "B": (2.7, 73),
        "B-": (2.3, 66),
        "C+": (2.0, 60),
        "C": (1.7, 53),
        "C-": (1.3, 46),
        "D+": (1.0, 40),
        "D": (0.7, 33),
        "D-": (0.0, 0),
    }
    # Loop through list and apply the grade equation
    for grade in grades:
        if grade >= grade_table["A+"][0]:
            print(grade_table["A+"])
        elif grade >= grade_table["A"][0]:
            print(grade_table["A"])
        elif grade >= grade_table["A-"][0]:
            print(grade_table["A-"])
        elif grade >= grade_table["B+"][0]:
            print(grade_table["B+"])
        elif grade >= grade_table["B"][0]:
            print(grade_table["B"])
        elif grade >= grade_table["B-"][0]:
            print(grade_table["B-"])
        elif grade >= grade_table["C+"][0]:
            print(grade_table["C+"])
        elif grade >= grade_table["C"][0]:
            print(grade_table["C"])
        elif grade >= grade_table["C-"][0]:
            print(grade_table["C-"])
        elif grade >= grade_table["D+"][0]:
            print(grade_table["D+"])
        elif grade >= grade_table["D"][0]:
            print(grade_table["D"])
        elif grade >= grade_table["D-"][0]:
            print(grade_table["D-"])
        else:
            print(grade_table["E"])
