```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.2, 3.15, 3.0],
        'B': [2.85, 2.8, 2.75, 2.7],
        'B-': [2.55, 2.5, 2.45, 2.4],
        'C+': [2.15, 2.1, 2.05, 2.0],
        'C': [1.65, 1.6, 1.55, 1.5],
        'C-': [1.45, 1.4, 1.35, 1.3],
        'D+': [1.05, 1.0, 0.95, 0.9],
        'D': [0.65, 0.6, 0.55, 0.5],
        'D-': [0.45, 0.4, 0.35, 0.3],
        'E': [0.0, 0.0]
    }
    return [letter_grades.get(letter)[grade >= min(letter_grades[letter])]
            for letter, grade in zip('ABCDE', grades)]
```

The task is to generate a list of letter grades corresponding to a list of student GPAs. The solution employs a dictionary named `letter_grades` that maps letter grades to ranges of GPAs. The function iterates through each GPA and compares it to the ranges to determine the appropriate letter grade. The returned list is a transformation of the input GPA list.

This approach has a time complexity of `O(n)` since it requires iterating through the GPA list once and processing each GPA once to determine the letter grade. 

The space complexity is `O(1)` since it only uses a constant amount of extra space to store the returned list.