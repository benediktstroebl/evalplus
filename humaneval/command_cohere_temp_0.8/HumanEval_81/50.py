```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, None, None, None, None, None, None, None, None, None],
        'A': [3.7, 3.3, None, None, None, None, None, None, None, None],
        'A-': [3.3, None, None, None, None, None, None, None, None, None],
        'B+': [3.0, None, None, None, None, None, None, None, None, None],
        'B': [2.7, 2.3, None, None, None, None, None, None, None, None],
        'B-': [2.3, None, None, None, None, None, None, None, None, None],
        'C+': [2.0, None, None, None, None, None, None, None, None, None],
        'C': [1.7, 1.3, None, None, None, None, None, None, None, None],
        'C-': [1.3, None, None, None, None, None, None, None, None, None],
        'D+': [1.0, None, None, None, None, None, None, None, None, None],
        'D': [0.7, 0.0, None, None, None, None, None, None, None, None],
        'D-': [0.0, None, None, None, None, None, None, None, None, None],
        'E': [None, None, None, None, None, None, None, None, None, 0.0]
        }
    letter_grades = {key: value for key, value in letter_grades.items() if value is not None}
    return [letter_grades[round((grade - min(letter_grades[key]), key)] for grade in grades]
            for key in letter_grades if min(letter_grades[key]) <= max(grades) ]
```
### Explanation:
1. **Dictionary of Letter Grades**: The function starts by defining a dictionary called `letter_grades`. This dictionary maps a letter grade to a GPA range. For instance, the key 'A+' is mapped to a list of GPAs, ranging from 4.0 to None.
2. **Filtering Empty Ranges**: After creating the `letter_grades` dictionary, we use a list comprehension to filter out any ranges that are not defined. This is because the `letter_grades` dictionary initially contains lists that might have `None` values, indicating that there is no lower or upper limit for a particular grade. We only want to keep the ranges with defined limits, hence the filtering.
3. **Mapping Grades**: The main logic of the function happens in the `return` statement. Here, we iterate over each key (letter grade) in `letter_grades`, but only for keys where the limit is not `None` (i.e., there's a maximum limit on the GPA). This ensures that only the relevant grade ranges are considered.
4. **Mapping to Letter Grades**: For each GPA in the input `grades` list, we use the `round()` function to find the nearest lower bound of the GPA range. We then use this nearest lower bound to determine the corresponding letter grade.

The output of the function will be a list where each element represents the letter grade corresponding to the GPA of that student, with the closest grade definition