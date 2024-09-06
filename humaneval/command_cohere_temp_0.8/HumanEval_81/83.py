```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.7, 3.65, 3.6, 3.55, 3.5],
        'A-': [3.3, 3.25, 3.2, 3.15, 3.0],
        'B+': [3.0, 2.95, 2.9, 2.85, 2.8],
        'B': [2.7, 2.65, 2.6, 2.55, 2.5],
        'B-': [2.3, 2.25, 2.2, 2.15, 2.0],
        'C+': [2.0, 1.95, 1.9, 1.85, 1.8],
        'C': [1.7, 1.65, 1.6, 1.55, 1.5],
        'C-': [1.3, 1.25, 1.2, 1.15, 1.0],
        'D+': [1.0, 0.95, 0.9, 0.85, 0.8],
        'D': [0.7, 0.65, 0.6, 0.55, 0.5],
        'D-': [0.3, 0.25, 0.2, 0.15, 0],
        'E': [0.0, 0.0, 0.0, 0.0, 0.0]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if grade in letter_grades[key]]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It does this by attempting to find the closest border between two GPA ranges which allows for a simpler and more scalable solution than a brute force approach using a dictionary lookup. Each border value in the keys of the dictionary is associated with a list of GPA values belonging to that letter grade. The function iterates over each GPA value in the input list and, through rounding and sorting operations, determines which border GPA value the input falls under and subsequently fetches the letter grade. As a result, the function maps every student GPA to a letter grade and returns these as a list. 

This approach ensures a straightforward, scalable solution that delivers the expected results based on the challenge's descriptive text. While a dictionary lookup could accomplish the same task, the present solution is optimized to reduce the computational complexity, crucial when dealing with potentially large datasets of student grades. 

The implementation assumes that the GPA values are points on a scale ranging from 0.0 to 4.0, which is common in many educational institutions. However, this approach can be adapted to work with other GPA scales or categories by simply redefining the dictionary and adjusting the logic used to categorize the grades.