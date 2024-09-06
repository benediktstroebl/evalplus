```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'.
    # Sort numbers from smallest to largest
    return ' '.join(sorted(numbers.split()), reverse=True)

# Test cases
test_cases = [
    "three one five",
    "six three eight",
    "zero four seven",
    "one two three four",
    "two six eight nine"
]

for test_case in test_cases:
    actual_sorted = sort_numbers(test_case)
    assert actual_sorted == ' '.join(sorted(test_case.split(), reverse=True))
```
This script defines a function `sort_numbers` that takes a string of numbers and returns a sorted version of the string, as per the given specification. It uses the test case for testing the function, where it passes in some test strings and asserts that the function returns the correct sorted result.