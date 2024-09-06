
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

    # A list of letter grade to GPA mapping
    map_gpa = [['A+', 4.0], ['A', 3.7], ['A-', 3.3], ['B+', 3.0], ['B', 2.7], ['B-', 2.3], ['C+', 2.0], ['C', 1.7], ['C-', 1.3], ['D+', 1.0], ['D', 0.7], ['D-', 0.3], ['E', 0.0]]

    # List of letter grades
    letter_grade = []
    
    # Looping through the list of grades
    for grade in grades:
        
        # Assigning the current grade to a temporary variable
        current_grade = grade
        
        # Looping through the gpa to letter grade mapping
        for i in range(len(map_gpa)):
            
            # If the temporary variable is greater than the gpa in the list
            if current_grade >= map_gpa[i][1]:
                
                # Assign the letter grade to the letter grade list
                letter_grade.append(map_gpa[i][0])
                
                # Exit the loop
                break

    # Return the letter grade
    return letter_grade
