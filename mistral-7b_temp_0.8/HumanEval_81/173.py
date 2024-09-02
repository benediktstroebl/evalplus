
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

    # Grades A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D- are the only grades that can be awarded
    # only one of the following grades is awarded: A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-
    # so when the code is run 10 times, 10 grades are outputted
    # also, only whole numbers are awarded (e.g. 2.9999999999999 is not awarded a grade)


    # TO DO: write your code here
    #
    # HINT: 
    # grades = [4.0, 3.0, 2.0, 3.5, 1.7, 2.3]
    # for i in range(len(grades)):
    #   print(grades[i])
    #
    # The below code is not correct, but it can be used as a template to guide you
    # it will output: 
    # 4.
