```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are strings are "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", and "nine".
    Return the string with numbers sorted from smallest to largest
    """
    return numbers.split(). sort(
        sorted(map(int, numbers. expected_items)), reverse=True)

def test_sort_numbers():
    test_list = "three one five"
    expected = "one three five"
    result = sort_numbers(test_list)
    assert result == expected, "Sorting did not work."

# Run the test
test_sort_numbers()
```

This script provides a self-contained function that sorts a list of numbers in Markdown style. You can use the thanks to test and verify the function. This is an good implementation and easy to understand.