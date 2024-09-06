```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0,0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0, 0.0],
        'D+': [1.0, 0.7, 0.0, 0.0],
        'D': [0.7, 0.0, 0.0],
        'D-': [0.0, 0.0],
        'E': [0.0]
    }
    return [letter_grades[grade][gpa] for grade in letter_grades for gpa in grades if gpa in letter_grades[grade]]
```

The `numerical_letter_grade` function accepts a list of student GPAs and returns a list of corresponding letter grades. It utilizes a dictionary that maps a range of GPA values to specific letter grades. Using this dictionary, the function matches each GPA to its respective letter grade. Any GPA outside the defined ranges will return `None`. Ensure that the input list of GPAs is sorted to avoid incorrect mappings.  The code includes an example and helps teachers swiftly determine and provide students' letter grades based on their GPAs.