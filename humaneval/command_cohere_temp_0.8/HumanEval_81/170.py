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
    return [letter_grades.get(grade)[round(grades[i]-min(grade_range), 1)] for i, grade_range in enumerate(letter_grades.values()) for grade in grades if grade in grade_range]
```
The code block provides a function called `numerical_letter_grade()` that takes in a list of student GPA scores and returns a list of corresponding letter grades based on the grading scale provided. The grading scale is defined using a dictionary where each key is a letter grade and each value is a list of GPA scores that correspond to that grade. The function uses this grading scale to determine the letter grades for each student GPA score in the input list. 

Let's break down the solution and discuss its components:
1. **Dictionary of Letter Grades**: The solution begins by defining a dictionary called `letter_grades`. This dictionary serves as a mapping between letter grades and GPA ranges for each grade. The GPA ranges are specified as lists because there can be fractional GPA values within a specific grade range.
2. **Grades Dictionary Lookup**: The core of the solution lies in using the `letter_grades` dictionary to map the input GPA scores to their corresponding letter grades. The code uses the GPA ranges as both the keys and the values in the dictionary to facilitate lookup.
3. **List Comprehension with Dictionary Lookup**: The solution uses a list comprehension to loop through the input `grades` list. Within each iteration, it checks if the current GPA score falls within one of the GPA ranges for a specific letter grade. The `grade in grade_range` condition checks if the GPA score is within the range for a particular grade.
4. **Round-off and Chaining**: To handle fractional GPA scores within a grade range, the solution uses the `round()` function to round off the difference between the GPA score and the minimum of the grade range. This ensures the correct position of the GPA within the range. Additionally, the `get()` method is used to retrieve the relevant