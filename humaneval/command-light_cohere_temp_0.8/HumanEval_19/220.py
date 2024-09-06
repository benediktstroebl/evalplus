Here's a Python script that includes the `sort_numbers` function along with the test cases:
```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))

# Test cases
test_cases = [
    "three one five",
    "zero one three four five",
    "two three seven eight nine",
    "six four nine",
    "one three eight nine ten"
]

for case in test_cases:
    assert sort_numbers(case) == case.
``` 
This code defines a function `sort_numbers` that takes a string of numbers in space separated format as input and returns a string of numbers sorted from smallest to largest in ascending order. The test cases are defined to validate the function's correctness.