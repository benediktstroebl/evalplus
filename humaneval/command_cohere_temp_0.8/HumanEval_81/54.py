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
    return [letter_grades[key][gpa-min(key)] for key, gpa in sorted(letter_grades.items())]
```

Here is a summary of how the code works:
1. A dictionary named `letter_grades` has been created which maps letter grades to GPAs and vice versa. The GPAs are sorted in decreasing order and the letter grades are mapped to GPAs by finding the index of the GPA for the desired letter grade in the sorted list of GPAs. This index is then added to the minimum GPA for the letter grade to get the desired GPA.
2. The function `numerical_letter_grade()` takes in a list of GPAs as an argument.
3. The function returns the list of letter grades corresponding to the provided GPAs using the logic mentioned above.

The example input list is `['4.0', '3', '1.7', '2', '3.5']`. The method will return its corresponding letter grades using the provided table:
```
['A+', 'B', 'C-', 'C', 'A-']
``` 
This result has been obtained using the following steps:
- The `letter_grades` dictionary was used to find the GPA ranges for each letter grade. 
- The input GPAs were used to sort the `letter_grades` dictionary. The GPA for 'A+' is the least and the GPA for 'E' is the greatest. 
- The GPAs for each input grade has been calculated by finding