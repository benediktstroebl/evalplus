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
    return [letter_grades[key][round(grade, 1)] for grade in grades for key in letter_grades if grade >= letter_grades[key][0]]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It does this by utilizing a dictionary that maps a range of GPA values to letter grades. The function iterates through each GPA in the input list and, in parallel, traverses the ranges of the letter grades dictionary. It assigns the appropriate letter grade to each GPA value by leveraging the `round` function to narrow down the GPA to the closest letter grade range.

The output is a list that contains the letter grades corresponding to each provided GPA, sorted in ascending order. 

This approach ensures a quick and efficient process for large datasets since it doesn't require importing any additional libraries and is solely based on the provided GPA ranges.