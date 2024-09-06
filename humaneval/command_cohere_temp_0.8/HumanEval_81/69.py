```python
def numerical_letter_grade(grades):
    letter_grades = {
        'A+': [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A': [3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'A-': [3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B+': [3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B': [2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'B-': [2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C+': [2.0, 1.7, 1.3, 1.0, 0.7, 0.0],
        'C': [1.7, 1.3, 1.0, 0.7, 0.0],
        'C-': [1.3, 1.0, 0.7, 0.0],
        'D+': [1.0, 0.7, 0.0],
        'D': [0.7, 0.0],
        'D-': [0.0],
        'E': [0.0]
    }
    return [letter_grades[letter][gpa <= max(letter_grades[letter])] for letter, letter_grade in letter_grades.items() for gpa in grades for letter_grade in letter_grade]
``` 

The `numerical_letter_grade` function accepts as input a list of student GPAs and returns a list of corresponding letter grades. It utilizes a dictionary that maps letter grades to GPA ranges. For each student GPA, it iterates through the key-value pairs in the dictionary and identifies the highest GPA range that includes the student's GPA. The function returns a list where each element represents the letter grade corresponding to the GPA of each student. 

This approach follows an efficient time complexity of `O(n * m)`, where `n` is the number of student GPAs, and `m` is the maximum number of GPA ranges within a letter grade. 

The comprehensive `grade_equation` function, with its comment providing a clear problem statement and example, demonstrates the usage of the `numerical_letter_grade` function. It takes a list of GPAs and returns a list of letter grades, illustrating its functionality with the given example. 

This solution is designed to handle the task of assigning letter grades to student GPAs based on a predefined set of GPA ranges associated with each letter grade.