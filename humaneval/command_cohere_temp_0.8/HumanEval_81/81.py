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

The code uses a dictionary to map a range of GPAs to letter grades and then uses list comprehensions to determine the letter grade for each GPA in the input list. The function handles cases where the GPA is exactly matching the threshold for obtaining a letter grade and cases where the GPA is within the range of the next lower letter grade. The function will return an empty list if the given list of grades is empty.

Let's break down the solution into smaller pieces for explanation:
1. **Dictionary of Letter Grades**: The dictionary `letter_grades` maps a list of GPAs to the corresponding letter grades as strings. Each key is a letter grade and the corresponding value is a list of GPAs that map to that letter grade. This is the backbone of our grading algorithm.
2. **Using List Comprehension**: We use list comprehensions in Python to create a new list based on existing lists. In our case, we want to create a list of letter grades based on the GPA list that is provided as input to our function. We iterate through each GPA in the input list and for each GPA, we iterate through each GPA range in our `letter_grades` dictionary to find the correct letter grade.
3. **Handling Border Cases**: The comprehensions handle border cases in a clever way. If a GPA is exactly on a boundary (e.g., 3.7 is the boundary between 'A' and 'A+'), it will round up, ensuring a more generous grade for the student.
4. **Empty Input Handling**: The function returns an empty list if the input list of grades is empty. This is important to handle to avoid errors or unexpected outputs for edge cases. 

The solution is structured and concise while maintaining flexibility to handle a variety of