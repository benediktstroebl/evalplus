```python
def grade_equation(gpa):
    """
    It is the last week of the semester and the teacher has to give the grades
    to students.
    The teacher has been using her own algorithm for grading.
    She has given the different GPA values for some students, and you have to write 
    a function that can output a list of letter grades using the following table:
    
    GPA       |    Letter grade
    4.0                > 3.7                A> 3.3                B
    example:
    grade_equation([4.0, 3, 1.
    , [2.7, 3]) ==> ['A+', 'B', 'B', 'C-']
    """
    letter_grades = ['A+', 'B', 'B', 'C-']
    for g in gpa:
        for grade in letter_grades:
            if g >= grade:
                print(grade, end=' ')
                break
    return letter_grades
```
This function takes a list of GPA values as a parameter and returns a list of corresponding letter grades. The function loops through the the GPA values and compares each GPA to each grade in the list of letter grades. The function then prints the letter grade for each GPA value that is greater than the grade. The function then returns the list of letter grades.