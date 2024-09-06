
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
    # Your code here
    
    #initialize the letter grade list
    letter_grade_list = []
    
    #loop through the grades list
    for grade in grades:
        
        #if the grades are A+
        if grade == 4:
            letter_grade_list.append("A+")
        #if the grades are A 
        elif grade > 3.7:
            letter_grade_list.append("A")
        #if the grades are A- 
        elif grade > 3.3:
            letter_grade_list.append("A-")
        #if the grades are B+
        elif grade > 3.0:
            letter_grade_list.append("B+")
        #if the grades are B 
        elif grade > 2.7:
            letter_grade_list.append("B")
        #if the grades are B-
        elif grade > 2.3:
            letter_grade_list.append("B-")
        #if the grades are C+
        elif grade > 2.0:
            letter_grade_list.append("C+")
        #if the grades are C
        elif grade > 1.7:
            letter_grade_list.append("C")
        #if the grades are C-
        elif grade > 1.3:
            letter_grade_list.append("C-")
        #if the grades are D+ 
        elif grade > 1.0:
            letter_grade_list.append("D+")
        #if the grades are D 
        elif grade > 0.7:
            letter_grade_list.append("D")
        #if the grades are D-
        elif grade > 0.3:
            letter_grade_list.append("D-")
        #if the grades are E
        elif grade >= 0:
            letter_grade_list.append("E")
            
    #return the letter grade list
    return letter_grade_list
