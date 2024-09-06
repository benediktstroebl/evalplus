
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
    
    # Loop through the grades and calculate the GPA
    for grade in grades:
        gpa = grade
    
    # Loop through the GPA and find the corresponding letter grade
    for i in range(len(gpa)):
        if gpa[i] > 3.7:
            letter_grades.append('A')
            break
        elif gpa[i] > 3.3:
            letter_grades.append('A-')
            break
        elif gpa[i] > 3.0:
            letter_grades.append('B')
            break
        elif gpa[i] > 2.7:
            letter_grades.append('B-')
            break
        elif gpa[i] > 2.0:
            letter_grades.append('C')
            break
        elif gpa[i] > 1.7:
            letter_grades.append('C')
            break
        elif gpa[i] > 1.3:
            letter_grades.append('C-')
            break
        elif gpa[i] > 1.0:
            letter_grades.append('D')
            break
        elif gpa[i] > 0.7:
            letter_grades.append('D')
            break
        elif gpa[i] > 0.0:
            letter_grades.append('F')
            break
    
    # Append the remaining grades (if any)
    for i in range(len(grades)):
        if not letter_grades:
            letter_grades.append('F')
        else:
            letter_grades.append(grades[i])
    
    return letter_grades
