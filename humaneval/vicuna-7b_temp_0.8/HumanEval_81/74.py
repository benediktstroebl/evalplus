
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
    # Create a dictionary to count the number of students in each GPA range
    gpa_ranges = {'4.0': 1, '3.7': 1, '3.3': 1, '3.0': 1, '2.7': 1,
                   '2.3': 1, '2.0': 1, '1.7': 1, '1.3': 1, '1.0': 1, '0.7': 1,
                   '0.0': 1, '0.3': 1, '0.0': 1}
    
    # Count the number of students in each GPA range and use the results to calculate
    # the letter grades
    for grade in grades:
        gpa = grade
        count = 0
        while gpa >= 0:
            gpa -= 0.1
            count += 1
        letter_grade = 'E' if count == 0 else (grade_combinations[gpa_ranges[f'{gpa:.2f}']][1] if gpa_ranges[f'{gpa:.2f}'] in grade_combinations else grade_combinations[gpa_ranges[f'{gpa:.2f}']][0])
           
        # Add the letter grade to the list and remove the GPA from the count
        grades.append(letter_grade)
        gpa_ranges[f'{gpa:.2f}'] -= 1
    
    return grades