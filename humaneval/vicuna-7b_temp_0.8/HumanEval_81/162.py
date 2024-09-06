
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

    # Creating an empty list to store the final grades
    letter_grades = []

    # Iterating through the list of GPAs
    for gpa in grades:
        # Making a list of numbers from GPA to 4.0
        gpa_numbers = [x if x >= gpa else 0 for x in range(1, 5) if x != gpa]

        # Checking which category the GPA falls into
        category = 'A'
        if gpa_numbers.count(gpa) == 1:
            category += '+'
        elif gpa_numbers.count(gpa) == 2:
            category += 'A'
        elif gpa_numbers.count(gpa) == 3:
            category += 'B'
        elif gpa_numbers.count(gpa) == 4:
            category += 'B+'
        elif gpa_numbers.count(gpa) == 5:
            category += 'A'
        elif gpa_numbers.count(gpa) == 6:
            category += 'B'
        else:
            category += 'C'

        # Adding the category to the final list of letter grades
        letter_grades.append(category)

    return letter_grades
