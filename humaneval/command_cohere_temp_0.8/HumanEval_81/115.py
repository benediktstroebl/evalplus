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
    return [letter_grades.get(letter)[gpa >= min(letter_grades[letter])] for letter, letter_grades in letter_grades.items() for gpa in grades]
```

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It utilizes a dictionary that maps a range of GPA values to specific letter grades. Using this dictionary, it checks each GPA value against the specified range for each letter grade and assigns the corresponding letter grade to the student's entry in the returned list.

Let's break down the solution into components to better understand how it works in detail:
1. `letter_grades` dictionary: 
    - This is a dictionary that maps specific GPA ranges to letter grades.
    - Each letter grade is assigned a list of GPAs that fall within its range. 
    - This ensures that the algorithm can swiftly find the correct letter grade for each GPA.
2. `return [letter_grades.get(letter)[gpa >= min(letter_grades[letter])] for letter, letter_grades in letter_grades.items() for gpa in grades]`:
    - This is the heart of the solution, a generator expression, that goes through each GPA and each letter grade, determining the correct letter grade for each GPA. 
    - For each GPA, we first determine the current letter grade letter (`letter`), and the corresponding GPA range (`letter_grades`). 
    - We then check if the GPA is greater than or equal to the minimum GPA in that range (`min(letter_grades[letter])`), indirectly providing the correct letter grade for that GPA. 
    - Finally, we use `get()` to retrieve the list of grades for the corresponding letter and select the correct letter using the GPA check, giving us the final letter grade for each student. 

The solution is optimized for efficiency, with the dictionary providing quick access to the relevant GPA ranges for each letter grade. The generator expression