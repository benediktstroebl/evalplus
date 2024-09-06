```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0,0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0, 0.0],
        'D+': [1.0, 0.7, 0.0, 0.0],
        'D': [0.7, 0.0, 0.0],
        'D-': [0.0, 0.0],
        'E': [0.0]
    }
    return [letter_grades[grade][gpa] for grade in letter_grades for gpa in grades if gpa in letter_grades[grade]]
```
The task is to implement a function `numerical_letter_grade` that takes a list of student GPAs and returns a list of letter grades for each student based on the given grading table. The function uses a dictionary to map a range of GPA values to specific letter grades and then returns the appropriate letter grade for each student's GPA. 

Let's break down how the code works:
1. **Dictionary of Letter Grades**: The core of this problem is a dictionary that maps a variety of GPA ranges to their corresponding letter grades. This dictionary is listed inline in the function but is also broken out into a separate dictionary `letter_grades` for easier readability.
2. **The main Function**: The function `numerical_letter_grade` takes a list of student GPAs as input. For each GPA in the input list, it iterates through the `letter_grades` dictionary to find the matching letter grade category.
3. **List Comprehension**: The list comprehension in the return statement combines the GPA input list with the dictionary lookup, checking if each GPA falls into a specific letter grade range. It returns the list of letter grades for the given GPAs.

The function is self-contained and doesn't rely on any external variables or additional code. It provides the requested functionality of converting a list of GPAs to a list of letter grades based on the given grading table.