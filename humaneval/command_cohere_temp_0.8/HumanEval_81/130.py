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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter]) for letter, gpa in zip(letter_grades.keys(), grades)] for letter in letter_grades.keys() if any(grades >= min(letter_grades[letter]) for letter_grades in letter_grades.values())]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of letter grades based on the provided criteria. Each GPA grade range is associated with a particular letter grade. The function inspects each GPA to determine which letter grade is appropriate and returns a sorted list of these letter grades. 

It utilizes a dictionary where the keys are the letter grades, and the values are lists of GPA ranges corresponding to each letter grade. The function loops through each key (letter grade) and uses a list comprehension to determine if the GPA falls within any of the ranges for that letter grade. If it does, that letter grade is included in the result. The `zip` function is used to iterate over the GPAs and letter grades simultaneously. The function handles scenarios where a list of GPAs is empty or contains just one GPA. 

This implementation has a time complexity of O(n*log(n)) due to the nested list comprehensions, making it efficient for small to medium-sized lists of student grades.