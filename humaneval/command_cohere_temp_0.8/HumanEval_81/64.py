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
    return [letter_grades[grade][idx] for idx, grade in enumerate(grades) ]
``` 

The code defines a Python function called `numerical_letter_grade` that takes a list of student GPA scores as input and returns a list of corresponding letter grades based on a predefined grading scale. The function uses a dictionary that maps GPA scores to letter grades to determine the correct letter grade for each student's GPA score. 

The grading scale is defined in the code using a list of GPA scores and their corresponding letter grades. The list is sorted in ascending order based on the GPA scores, with the highest GPA scores at the beginning of the list. 

The function iterates through the list of student GPA scores, and for each score, it finds the corresponding letter grade in the grading scale using the `enumerate` function. The `enumerate` function provides both the index `idx` of the GPA score in the list and its corresponding letter grade. 

The function returns a list of letter grades for each student based on their GPA scores. 

The code is self-contained, meaning that it contains all the necessary logic and data to perform the grading calculation within the function, and it can be executed independently without relying on external variables or functions. 

This approach allows the function to be easily reused and integrated into different projects or scripts that require calculating letter grades from GPA scores based on this grading scale. 

The function can be tested by calling it with different lists of GPA scores and comparing the generated letter grades with the expected outputs based on the grading scale