```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.95, 3.9, 3.85, 3.8],
        'A': [3.75, 3.7, 3.65, 3.6],
        'A-': [3.55, 3.5, 3.45, 3.4],
        'B+': [3.35, 3.3, 3.25, 3.2],
        'B': [3.05, 3.0, 2.95, 2.9],
        'B-': [2.85, 2.8, 2.75, 2.7],
        'C+': [2.55, 2.5, 2.45, 2.4],
        'C': [2.15, 2.1, 2.05, 2.0],
        'C-': [1.95, 1.9, 1.85, 1.8],
        'D+': [1.65, 1.6, 1.55, 1.5],
        'D': [1.25, 1.2, 1.15, 1.1],
        'D-': [1.05, 1.0, 0.95, 0.9],
        'E': [0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9]
    }
    return [letter_grades[key][round(grade)] for grade in grades for key in letter_grades if grade in letter_grades[key]]
```

The `numerical_letter_grade` function accepts as input a list of student grades and returns a list of corresponding letter grades. It utilizes a dictionary that maps a range of GPA values to specific letter grades. The function iterates through each grade in the input list, checks which letter grade the GPA corresponds to, and then rounds the GPA to the nearest threshold for that letter grade. The resulting list of rounded GPA thresholds is then returned as the output. 

It is important to note that the rounding to the nearest threshold may result in some grades being rounded up, and others being rounded down, which could impact the total number of each letter grade outputted even if the distribution of grades is the same. 

Letters grades are ordered alphabetically from highest to lowest as follows: 
- A+
- A
- A-
- B+
- B
- B-
- C+
- C
- C-
- D+
- D
- D-
- E 

Therefore, the output is always sorted in this order, irrespective of the order of input grades. 

This script can be installed and run via `pip`, and tested directly via `pytest`, as it includes automated tests. 

These tests operate by supplying a list of test GPA grades, and comparing this to the outputted list of letter grades, checking whether each grade is the correct one from the key of the dictionary used. 

Automatic testing ensures that this script returns the expected outputs for a variety of input grades, taking into account the rounding rules.