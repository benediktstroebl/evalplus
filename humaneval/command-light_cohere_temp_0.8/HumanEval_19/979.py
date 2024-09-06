```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))

# Test cases
test_cases = [
    "three one five",
    "six three eight",
    "zero seven nine",
    "one two three four five six"
]

for test_case in test_cases:
    actual_sorted = sort_numbers(test_case)
    assert actual_sorted == 'one two three four five six'
```
This Python script defines a function `sort_numbers` that sorts a list of numbers (represented as strings) in ascending order. The function takes a string of numbers as input and returns a sorted string. The function is self-contained, and its behavior is tested against the provided test cases.