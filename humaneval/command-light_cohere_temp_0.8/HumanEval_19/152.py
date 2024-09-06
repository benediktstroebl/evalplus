Certainly! Here is a Python script with a self-contained function that solves the problem you described:

```python
import typing
from typing import List


def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    """
    numbers = [int(num) for num in numbers.
    return ''.join(sorted(numbers))

# Test cases
def test_sort_numbers():
    test_str = "three one five"
    expected = "one three five"
    got = sort_numbers(test_str)
    assert got == expected, f"Expected '{expected}', but got '{got}'"


# Run the function and test cases
test_sort_numbers()
```

This script defines a function `sort_numbers` that sorts a list of numbers from the smallest to the largest. The test case `test_sort_numbers` verifies that the function's output matches the expected result. You can further customize the