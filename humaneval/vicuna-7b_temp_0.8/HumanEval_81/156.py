
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
    # sort grades in ascending order
    sorted_grades = sorted(grades)

    # return empty list if there are no grades or no 4.0 GPA
    if not sorted_grades or sorted_grades[0] < 4.0:
        return []

    # initialize result list
    result = []

    # check if there is a 4.0 GPA
    if sorted_grades[0] == 4.0:
        # if there is a 4.0 GPA, add 'A+' to the result list
        result.append('A+')
    else:
        # if there is not a 4.0 GPA, check if there is a 3.7 GPA
        for grade in sorted_grades:
            if grade == 3.7:
                result.append('A')
                break
        else:
            # if there is no 3.7 GPA, check if there is a 3.3 GPA
            for grade in sorted_grades:
                if grade == 3.3:
                    result.append('A-')
                    break
            else:
                # if there is no 3.3 GPA, check if there is a 3.0 GPA
                for grade in sorted_grades:
                    if grade == 3.0:
                        result.append('B')
                        break
                    elif grade == 2.7:
                        result.append('B-')
                        break
                    elif grade == 2.3:
                        result.append('C')
                        break
                    elif grade == 1.7:
                        result.append('C-')
                        break
                    elif grade == 1.3:
                        result.append('C')
                        break
                    elif grade == 1.0:
                        result.append('D')
                        break
                    elif grade == 0.7:
                        result.append('D-')
                        break
                    elif grade == 0.0:
                        result.append('E')
                        break
    return result
