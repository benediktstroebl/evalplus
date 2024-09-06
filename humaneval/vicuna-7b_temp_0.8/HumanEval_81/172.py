
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
    #sort the grades in descending order
    grades = sorted(grades, reverse=True)
    
    #create an empty list to store the letter grades
    letter_grades = []
    
    #loop through the grades and append the letter grade
    for grade in grades:
        #check if the grade is greater than or equal to 3.0
        if grade >= 3.0:
            #check if the grade is greater than 3.3
            if grade > 3.3:
                letter_grades.append('A')
            #check if the grade is greater than or equal to 3.0
            elif grade >= 3.0:
                letter_grades.append('A-')
            #check if the grade is greater than or equal to 2.7
            elif grade >= 2.7:
                letter_grades.append('B')
            #check if the grade is greater than or equal to 2.3
            elif grade >= 2.3:
                letter_grades.append('B-')
            #check if the grade is greater than or equal to 2.0
            elif grade >= 2.0:
                letter_grades.append('C')
            #check if the grade is greater than or equal to 1.7
            elif grade >= 1.7:
                letter_grades.append('C')
            #check if the grade is greater than or equal to 1.3
            elif grade >= 1.3:
                letter_grades.append('C-')
            #check if the grade is greater than or equal to 1.0
            elif grade >= 1.0:
                letter_grades.append('D')
            #check if the grade is greater than or equal to 0.7
            elif grade >= 0.7:
                letter_grades.append('D-')
            #check if the grade is greater than or equal to 0.0
            elif grade >= 0.0:
                letter_grades.append('E')
        else:
            #check if the grade is greater than or equal to 0.0
            if grade >= 0.0:
                letter
