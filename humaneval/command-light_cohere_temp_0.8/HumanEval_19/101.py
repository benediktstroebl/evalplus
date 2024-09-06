```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    numbers = [0, 2, 3, 4, 5]
    string = "".join(sorted(numbers))
    return string

# Test cases
test_cases = [
    "three one five",
    "six three",
    "zero seven eight nine",
    "two three four five six",
]

for i, test_case in enumerate(test_cases):
    actual = sort_numbers(test_case)
    expected = [i, 4, 1, 5]
    assert actual == expected, f"Case {i+1} not valid"
 ``` 
This code defines a function sort_numbers that sorts a space-separated string of numbers. It takes a numbers, and then sorts them from smallest to largest, and returns a sorted string. The code also provides several test cases to check if the function is working correctly.