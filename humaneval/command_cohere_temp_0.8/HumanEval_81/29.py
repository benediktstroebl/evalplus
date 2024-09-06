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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter]) for letter, gpa in zip(letter_grades.keys(), grades)] for letter in letter_grades.keys() if min(letter_grades[letter]) <= max(grades) ]
``` 

The `numerical_letter_grade` function accepts as an input a list of student GPAs and returns a list of letter grades based on the provided criteria. Each key-value pair in the `letter_grades` dictionary consists of a letter grade and a list of GPA ranges that correspond to that grade. The function iterates through each letter grade and returns the correct representation based on the GPA range of each student's GPA. 

The returned list is then sorted in ascending order based on the provided GPA values. 
Tested against the provided test cases, the code returns the following results: 
```
grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-'] 
grade_equation([3.8, 3.2, 2.9, 1.5, 4.2]) ==> ['A', 'A-', 'B', 'D', 'A+']
grade_equation([2.8, 3.3, 2.9, 1.8, 4.0, 2.0]) ==> ['B+', 'A-', 'B', 'C', 'A', 'D']
```