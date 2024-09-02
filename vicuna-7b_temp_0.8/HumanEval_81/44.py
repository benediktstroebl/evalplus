
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
    # Create an empty list to store the letter grades
    letter_grades = []
    # Loop through the list of GPAs
    for gpa in grades:
        # Create a list of all possible letter grades
        letter_grades_list = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'D', 'E']
        # Create a list of all possible GPA ranges
        gpa_ranges = [['>= '.0 * (i+1), '<= '.0 * (i+2)] for i in range(6, 13)]
        # Loop through the list of possible GPA ranges
        for grade_range in gpa_ranges:
            # Loop through the list of possible letter grades
            for letter_grade in letter_grades_list:
                # If the current GPA is in the current GPA range, add the letter grade
                # to the list of letter grades and remove the GPA range from the list
                if gpa >= grade_range[0] and gpa <= grade_range[1]:
                    letter_grades.append(letter_grade)
                    gpa_ranges.remove(grade_range)
    return letter_grades