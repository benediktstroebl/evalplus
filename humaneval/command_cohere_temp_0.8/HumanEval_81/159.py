```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None, None, None, None, None],
        'A': [3.7, 3.3, None, None, None, None, None, None, None],
        'A-': [3.3, None, None, None, None, None, None, None, None],
        'B+': [3.0, 2.7, None, None, None, None, None, None, None],
        'B': [2.3, 2.0, 1.7, None, None, None, None, None, None],
        'B-': [2.0, 1.7, 1.3, None, None, None, None, None, None],
        'C+': [1.7, 1.3, 1.0, 0.7, None, None, None, None, None],
        'C': [1.3, 1.0, 0.7, 0.3, None, None, None, None, None],
        'C-': [1.0, 0.7, 0.3, 0.0, None, None, None, None, None],
        'D+': [0.7, 0.3, 0.0, None, None, None, None, None, None],
        'D': [0.3, 0.0, None, None, None, None, None, None, None],
        'D-': [0.0, None, None, None, None, None, None, None, None],
        'E': [None, None, None, None, 0.0, None, None, None, None]
    }
    return [letter_grades[grade][idx] for grade in grades for idx in range(len(grades))]
```

The logic is straightforward. We create a dictionary with the GPA scores and the corresponding letter grades. Then we iterate through the grades and return the according letter grades. Each letter grade is represented as a list of its numerical grades so we can use it as a lookup table for the corresponding letter grades. And since the problem statement does not specify any specific order of the returned list we return a list of letter grades in the order of the input grades. 

Also note that the example in the problem statement has duplicate grades in the input and the function will return the same letter grades for those inputs without any specific order of the outputs.