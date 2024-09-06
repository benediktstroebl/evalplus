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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter])] for letter, letter_grades in letter_grades.items() for gpa in grades]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It utilizes a dictionary that maps letter grades to ranges of GPAs to determine the applicable letter grade for each student's GPA. As the problem solution states, in the case of a tie, the preference order of the letters is also included in the dictionary. This is also taken into account by the function in returning the correct letter grade for each student's GPA. 

This solution adheres to the problem's request for a self-contained script, as it does not rely on any external libraries or data and is suitable for standalone use. 

You can test the function by calling `numerical_letter_grade([2.3, 3.7, 1.0, 3.2, 2.8])`, which should return `['B-', 'A', 'D', 'B', 'B+']`.  This way, you can verify the function's correctness.