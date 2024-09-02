
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
    # Create a dictionary to store the letter grades and the corresponding GPA points
    letter_grades = {
        'A+': 4.25,
        'A': 3.75,
        'A-': 3.5,
        'B+': 3.25,
        'B': 3.0,
        'B-': 2.75,
        'C+': 2.5,
        'C': 2.25,
        'C-': 2.0,
        'D+': 1.75,
        'D': 1.5,
        'D-': 1.25,
        'D': 1.0,
        'F': 0.0
    }
    
    # Check if any GPA is below 0.0
    if any(gpa < 0.0 for gpa in grades):
        return ['F']
    
    # Check if any GPA is below 1.0
    if any(gpa < 1.0 for gpa in grades):
        return ['D-', 'D', 'D+'] + [letter_grades[gpa] for gpa in grades if gpa >= 1.0]
    
    # Check if any GPA is below 2.0
    if any(gpa < 2.0 for gpa in grades):
        return ['C-', 'C', 'C+'] + [letter_grades[gpa] for gpa in grades if gpa >= 2.0]
    
    # Check if any GPA is below 3.0
    if any(gpa < 3.0 for gpa in grades):
        return ['B-', 'B', 'B+'] + [letter_grades[gpa] for gpa in grades if gpa >= 3.0]
    
    # Check if any GPA is below 4.0
    if any(gpa < 4.0 for gpa in grades):
        return ['C+', 'C', 'C-', 'C', 'B-', 'B', 'B+', 'A-']
