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
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if round(grade) in letter_grades[key]]
```

The `numerical_letter_grade` function accepts a list of student grades as input and uses a dictionary of GPA ranges and corresponding letter grades to determine the letter grade for each student. The function then returns a list of the calculated letter grades in the same order as the input list of student grades.

Let's break down the solution into its main components:
1. **Dictionary of Letter Grades**: The solution begins by defining a dictionary that maps a range of GPAs to specific letter grades. Each letter grade is associated with a list of possible GPAs that correspond to it.
2. **Mapping the Grades**: For each student's GPA in the input list, the code iterates through the GPA ranges in the letter_grades dictionary. The GPA range is checked using the `round()` function, ensuring the GPA is rounded to the nearest hundredth. This helps when comparing the student's GPA to the GPAs in the letter_grades dictionary.
3. **Returning the Results**: For each student's GPA, the code finds the first key in the `letter_grades` dictionary whose GPA range contains the rounded GPA. The corresponding letter grade is then returned for that student's GPA. This happens in the line: `return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if round(grade) in letter_grades[key]]`.

By leveraging the `round()` function and specific GPA ranges in the `letter_grades` dictionary, the solution effectively determines the appropriate letter grade for each student's GPA. The final output is a list of these calculated letter grades, which is returned by the function.