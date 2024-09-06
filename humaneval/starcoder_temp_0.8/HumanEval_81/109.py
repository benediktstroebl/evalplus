
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
    lst = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_lst = []
    for i in grades:
        if i >= 4:
            new_lst.append(lst[0])
        elif i >= 3.7:
            new_lst.append(lst[1])
        elif i >= 3.3:
            new_lst.append(lst[2])
        elif i >= 3.0:
            new_lst.append(lst[3])
        elif i >= 2.7:
            new_lst.append(lst[4])
        elif i >= 2.3:
            new_lst.append(lst[5])
        elif i >= 2.0:
            new_lst.append(lst[6])
        elif i >= 1.7:
            new_lst.append(lst[7])
        elif i >= 1.3:
            new_lst.append(lst[8])
        elif i >= 1.0:
            new_lst.append(lst[9])
        elif i >= 0.7:
            new_lst.append(lst[10])
        elif i >= 0.0:
            new_lst.append(lst[11])
        elif i >= 0.0:
            new_lst.append(lst[12])
    return new_lst
