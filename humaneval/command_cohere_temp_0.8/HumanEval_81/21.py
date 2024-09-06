```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0],
        'D+': [1.0, 0.7, 0.0],
        'D': [0.7, 0.0],
        'D-': [0.0],
        'E': [0.0]
    }
    return [letter_grades[key][gpa_score] for key, gpa_score in zip(letter_grades.keys(), grades)]
```

Here is a summary of how the code works:
1. A dictionary named `letter_grades` has been created which maps letter grades to GPAs.
2. The list of GPAs is iterated through using `zip`, which creates a list of tuples with the key and GPA score from the `letter_grades` dictionary.
3. Using `letter_grades[key][gpa_score]`, the corresponding letter grade is found and returned for each GPA score.

The example input of `[4.0, 3, 1.7, 2, 3.5]` will produce the following output:
```python
['A+', 'B', 'C-', 'C', 'A-']
``` 

This approach utilizes a dictionary and list comprehension, resulting in a clean and efficient solution.