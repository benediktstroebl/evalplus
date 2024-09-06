
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
    #initialize empty list
    letter_grades = []
    
    #check if there is a student with GPA less than 0
    for student in grades:
        if student[1] < 0:
            return []
    
    #check if there is a student with GPA greater than 4.0
    for student in grades:
        if student[1] > 4.0:
            return []
    
    #iterate through the list of grades
    for i in range(len(grades)):
        #get the GPA of the current student
        gpa = grades[i][1]
        
        #check if the GPA is greater than 3.7
        if gpa > 3.7:
            letter_grades.append('A')
        #check if the GPA is greater than 3.3
        elif gpa > 3.3:
            letter_grades.append('A-')
        #check if the GPA is greater than 3.0
        elif gpa > 3.0:
            letter_grades.append('B')
        #check if the GPA is greater than 2.7
        elif gpa > 2.7:
            letter_grades.append('B-')
        #check if the GPA is greater than 2.0
        elif gpa > 2.0:
            letter_grades.append('C')
        #check if the GPA is greater than 1.7
        elif gpa > 1.7:
            letter_grades.append('C')
        #check if the GPA is greater than 1.3
        elif gpa > 1.3:
            letter_grades.append('C')
        #check if the GPA is greater than 1.0
        elif gpa > 1.0:
            letter_grades.append('D')
        #check if the GPA is greater than 0.7
        elif gpa > 0.7:
            letter_grades.append('D')
        #check if the GPA is equal to 0.0
        elif gpa == 0.0:
           
