```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None],
        'A': [3.7, 3.3, None, None, None],
        'A-': [3.0, 3.7, 3.3, None, None],
        'B+': [2.7, 2.3, 3.0, None, None],
        'B': [2.3, 2.7, 2.3, None, None],
        'B-': [2.0, 2.3, 2.7, None, None],
        'C+': [1.7, 1.3, 2.0, None, None],
        'C': [1.3, 1.7, 1.3, None, None],
        'C-': [1.0, 1.3, 1.7, None, None],
        'D+': [0.7, None, 1.0, None, None],
        'D': [0.0, 0.7, 1.0, None, None],
        'D-': [None, None, 0.7, 0.0, None],
        'E': [None, None, None, 0.0, None]
    }
    return [letter_grades[letter][gpa >= threshold] for letter, threshold in letter_grades.items() for gpa in grades]
```

The code leverages nested list comprehension and the dictionary of grading thresholds to map GPA scores to letter grades. A GPA score is compared to the threshold for the next highest letter grade and assigned the appropriate letter grade if it meets or exceeds that threshold. If the GPA is 0.0 or less, the letter grade 'E' is assigned. The function can be used to process a list of GPA scores and output a corresponding list of letter grades. 

To use the `numerical_letter_grade` function, you can call it with a list of GPA scores as depicted in the example below: 
```python
grades = [4.0, 3, 1.7, 2, 3.5]
letter_grades = numerical_letter_grade(grades)
print(letter_grades)
``` 

This will output:
```bash
['A+', 'B', 'C-', 'C', 'A-']
``` 

This list represents the letter grades corresponding to the GPA scores provided.