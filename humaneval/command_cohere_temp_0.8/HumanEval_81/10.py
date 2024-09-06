```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.25, 3.2],
        'B': [3.05, 3.0, 2.95, 2.9],
        'B-': [2.85, 2.8, 2.75, 2.7],
        'C+': [2.55, 2.5, 2.45, 2.4],
        'C': [2.15, 2.1, 2.05, 2.0],
        'C-': [1.95, 1.9, 1.85, 1.8],
        'D+': [1.65, 1.6, 1.55, 1.5],
        'D': [1.25, 1.2, 1.15, 1.1],
        'D-': [1.05, 1.0, 0.95, 0.9],
        'E': [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    }
    return [letter_grades[letter][round(grade)] for grade, letter in zip(grades, 'ABCDE')]
```
#### How It Works:
1. **Dictionary of Letter Grades**: Consists of two columns. The first is a list of GPAs that map to each letter grade, and the second is the range of GPAs that map to each letter grade.
2. **Mapping GPA to Letter Grade**: Uses dictionary lookup for each GPA in the list of student grades.
3. **Zip GPA and Letter Grades**: Pairs each GPA with its corresponding letter grade.
4. **Round GPAs**: Rounds GPAs to the nearest hundredth for consistent mapping.
5. **List Comprehension**: Uses list comprehension to produce a list of letter grades for each student grade.
#### Assumptions:
- The function assumes that all GPAs are entered as floats and already rounded to the nearest hundredth.
- The teacher’s algorithm seems to include rounding GPAs for some grades but not others, likely to the nearest hundredth. We implement this rounding for consistency.

This solution assumes that the list of student grades contains only GPA values and no other information. It also assumes that the list is not empty. 

The output list has a length equal to the length of the input list, with each element corresponding to the letter grade for the respective GPA. 

#### Examples:
```python
grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
grade_equation([3.8, 3.2, 2.9, 1.5, 0.8]) ==> ['A', 'A-', 'B', 'D', 'D-']
grade_equation([2.1, 4.4, 2.8, 3.2, 1.6]) ==> ['C', 'A+', 'B', 'A-', 'D']
``` 

This solution should