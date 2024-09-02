
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
    #The student's GPA
    student_gpa = [g for g in grades]

    #Initialize the letter grade list
    letter_grade_list = []

    #Check if the student's GPA is 0
    if any(g == 0 for g in student_gpa):
        letter_grade_list.append('E')
    else:
        #Get the highest GPA in the list
        max_gpa = max(student_gpa)

        #Check if the max GPA is 4.0
        if max_gpa == 4.0:
            letter_grade_list.append('A+')
        #Check if the max GPA is greater than 3.7 and less than or equal to 4.0
        elif max_gpa > 3.7 and max_gpa <= 4.0:
            letter_grade_list.append('A')
        #Check if the max GPA is greater than 3.3 and less than or equal to 3.7
        elif max_gpa > 3.3 and max_gpa <= 3.7:
            letter_grade_list.append('A-')
        #Check if the max GPA is greater than 3.0 and less than or equal to 3.3
        elif max_gpa > 3.0 and max_gpa <= 3.3:
            letter_grade_list.append('B+' if max_gpa > 3.1 else 'B')
        #Check if the max GPA is greater than 2.7 and less than or equal to 3.0
        elif max_gpa > 2.7 and max_gpa <= 3.0:
            letter_grade_list.append('B-' if max_gpa > 2.6 else 'B')
        #Check if the max GPA is greater than 2.3 and less than or equal to 2.7
        elif max_gpa > 2.3 and max_gpa <= 2.7:
            letter_grade_list.append('C+' if max_gpa > 2.5 else 'C')
        #Check if the max
