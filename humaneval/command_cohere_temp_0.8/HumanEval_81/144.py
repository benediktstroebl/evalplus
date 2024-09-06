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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter]) for letter, gpa in zip('ABCDEF', grades)] for letter in 'ABCDEF' if min(letter_grades[letter]) > 0]
```
### Explanation:
- The dictionary `letter_grades` maps a letter grade to a list of GPAs for that letter grade or slightly lower, except for 'E' which maps to 0s.
- We iterate over each letter grade and for each GPA in the input list `grades`, we check if the GPA is at least as high as the minimum GPA for that letter grade or higher, and if it is, we include this letter grade in the resulting list. 
- The list comprehension inside the `zip` function pairs each GPA in `grades` with the corresponding letter grade, considering only letters for which `min(letter_grades[letter])` is greater than 0. 

The solution works by first creating a dictionary that maps each letter grade to a list of GPAs for students corresponding to that grade or slightly lower. We then use list comprehension and `zip` to pair each GPA in the input list with the GPAs in the letter grade lists. We include an entry in the output list if the GPA is equal to or higher than the minimum GPA for that letter grade.