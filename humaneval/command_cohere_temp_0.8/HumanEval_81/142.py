```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0],
        'D+': [1.0, 0.7, 0.0],
        'D': [0.7, 0.0],
        'D-': [0.0],
        'E': [0.0]
    }
    return [letter_grades[letter][gpa] for letter, gpas in letter_grades.items() for gpa in grades if gpa >= gpas[0] and gpa <= gpas[-1]]
```
The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It utilizes a dictionary where each letter grade is associated with a GPA range. The function traverses the GPA ranges for each letter grade and returns the appropriate letter grade for each student's GPA. For instance, with an input list of `[4.0, 3, 1.7, 2, 3.5]`, the output would be `['A+', 'B', 'C-', 'C', 'A-']`. The solution is designed to be self-contained, offering the complete grading algorithm within the function.