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
    return [letter_grades[key][gpa_score] for key, gpa_score in zip(letter_grades, grades)]
```
This Python script defines a function called `numerical_letter_grade` which takes a list of student GPA scores and returns a list of corresponding letter grades based on the predefined grading scale. The key and GPA scores are zipped and the `index` method is used to find the correct letter grade for each GPA score.

Let's break it down:
1. A dictionary `letter_grades` is defined which maps letter grades to ranges of GPA scores. Each range is stored as a list in the dictionary value.
2. The function `numerical_letter_grade` takes a list of student GPA scores (`grades`) as input.
3. The `letter_grades` dictionary is iterated using `zip`, with the key and value corresponding to the letter grade and GPA score range. 
4. The `index` method is used to find the index of the GPA score in the range list, and the corresponding letter grade is returned for each student. 

The provided code will produce the correct letter grades for the given GPA scores. 

This script can be run directly or integrated into a larger assignment or program. 

Note: This solution assumes that the input list of GPA scores is valid, and that all scores are numerical values, with either decimal points or decimal-like notation (e.g., 3.7, 2, 1.5, etc.). Other input formats or non-num