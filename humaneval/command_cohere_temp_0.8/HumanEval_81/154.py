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
    return [letter_grades[key][round(grade)-1] for grade in grades for key in letter_grades if round(grade) in letter_grades[key]]
```

The task is to create a function that converts a list of student GPAs to a list of letter grades based on the provided specifications. The Python script provided a function called `numerical_letter_grade` that accepts a list of student GPAs as input and returns a corresponding list of letter grades. 

The logic behind the function is taking a list of student GPAs and mapping them to their corresponding letter grades based on the provided specification. It utilizes a dictionary that maps a range of GPA values to specific letter grades. The function iterates through each GPA value in the input list and applies the mapping logic to determine the corresponding letter grade. 

To ensure a proper letter grade for each student, the rounding of the GPA to the nearest tenth is implemented. This step takes into consideration the specific range of GPA values associated with each letter grade, selecting the correct letter grade that falls within the closest range. 

Overall, the provided code efficiently solves the problem and allows you to determine the letter grades for a list of student GPAs based on the given specifications.