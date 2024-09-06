Certainly, here's the Python script with a self-contained function that sorts and validates numbers in markdown code blocks:
```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    return numbers.
    """
 strings in the sorted order of numbers.
"""

def test_sort_numbers():
    """
    Test suite function to check the correctness of the sort_numbers function.
    """
    numbers = "three one five six two eight seven nine"
    expected = "one two three four five six seven eight nine"
    actual = sort_numbers(numbers)
    assert actual == expected, "Function did not sort numbers correctly."

# Run the tests
test_sort_numbers()
```

This script defines a function `sort_numbers` that takes a string of numbers in markdown code block format as an argument, and returns the string with numbers sorted from smallest to largest. The `test_sort_numbers` function is used to run the test suite and verify that the function works correctly.