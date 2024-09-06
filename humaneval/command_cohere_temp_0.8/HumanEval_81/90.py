```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None],
        'A': [3.7, 3.3, None, None, None],
        'A-': [3.0, 3.7, 3.3, None, None],
        'B+': [2.7, 2.3, 3.0, None, None],
        'B': [2.3, 2.7, 2.3, 1.7, None],
        'B-': [2.0, 2.3, 2.7, 1.7, 1.3],
        'C+': [1.7, 1.3, 2.0, 1.3, None],
        'C': [1.3, 1.7, 1.3, 0.7, None],
        'C-': [1.0, 1.3, 1.7, 0.7, 0.3],
        'D+': [0.7, None, 1.0, 0.7, None],
        'D': [0.3, 0.7, None, 0.3, None],
        'D-': [0.0, 0.3, 0.7, 0.3, 0]]
    sorted_grades = sorted(grades)
    res = []
    for g in sorted_grades:
        letter_grade = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 
                       'C+', 'C', 'C-', 'D+', 'D', 'D-']
        index = letter_grades[letter_grade[0]].index(g)
        if index == 0:
            res.append(letter_grade[0])
        elif index == 1:
            res.append(letter_grade[1])
        elif index == 2:
            res.append(letter_grade[2])
        elif index == 3:
            res.append(letter_grade[3])
        elif index == 4:
            res.append(letter_grade[4])
        elif index == 5:
            res.append(letter_grade[5])
        elif index == 6:
            res.append(letter_grade[6])
        elif index == 7:
            res.append(letter_grade[7])
        elif index == 8:
            res.append(letter_grade[8])
        elif index == 9:
            res.append(letter_grade[9])
        else:
            res.append(letter_grade[10])
    return res
```

This Python code defines a function called `numerical_letter_grade` that takes a list of student GPA scores as input. It creates a dictionary that maps a range of GPA scores to letter grades. The function then sorts the input list of GPAs in ascending order. It iterates through the sorted list and uses the dictionary to determine the corresponding letter grade for each GPA score. The function returns a list of letter grades in the order of the input GPA scores.

Let's break down the key components of the code:
1. `letter_grades` dictionary: This dictionary serves as a lookup table that maps a range of GPA scores to specific letter grades. Each key is a letter grade, and the corresponding value is a list of the minimum GPA scores that qualify for that letter grade. This is the grading scale that the teacher has provided you with.
2. `sorted_grades` list: The input list of GPAs is sorted in ascending order. This