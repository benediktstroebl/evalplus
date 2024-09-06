
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

    # The letter grades for each range of GPA
    letter_grades = {
        'A+': 4.0,
        'A' : 3.7,
        'A-': 3.3,
        'B+': 3.0,
        'B' : 2.7,
        'B-': 2.3,
        'C+': 2.0,
        'C' : 1.7,
        'C-': 1.3,
        'D+' : 1.0,
        'D' : 0.7,
        'D-': 0.3,
        'E' : 0.0
    }
    
    # The list of letter grades for the students
    letter_grade_list = []
    
    # Loop through the grades given
    for gpa in grades:
        for letter_grade in letter_grades:
            # If the GPA given is greater than or equal to the GPA of a given letter grade
            if gpa >= letter_grades[letter_grade]:
                # Add that letter grade to the list of letter grades
                letter_grade_list.append(letter_grade)
                # break out of the loop so we don't keep looking
                break
    
    return letter_grade_list
    
