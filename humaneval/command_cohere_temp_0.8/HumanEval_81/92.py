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
    return [letter_grades[grade][idx] for idx, grade in enumerate(grades) ]
``` 

The function employs a dictionary of GPA-letter grade associations to determine the letter grade for each GPA value. Using the dictionary, the function translates each GPA value in the input list to its corresponding letter grade. The output is a list of letter grades in the same order as the input GPA list. 

This approach enables a quick retrieval and translation of GPA values into letter grades through dictionary lookups. The consequent list of letter grades is then returned. 

The `'A+'` grade is used for GPA values of 4.0 and above, `'A'` is used for GPA values between 3.7 and 3.3, etc. For GPA values below 0.7, the function assigns the `'E'` grade. The above mentioned grading scale is followed in the schema. 

The self-contained function is easy to use and understand. It takes a list of grades and returns a list of corresponding letter grades based on the specified grading scheme. The function is also efficient, with a time complexity of `O(n)` where `n` is the length of the input list. 

This approach showcases the practical application of Python dictionaries and lists to solve a real-world problem related to data mapping and translation.  It can be used by teachers or schools to automate the assignment of letter grades based on GPA scores.