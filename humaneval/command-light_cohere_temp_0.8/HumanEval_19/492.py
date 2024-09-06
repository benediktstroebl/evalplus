```python
import pytest
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine,
    Valid choices are zero, one, two, three, four, five, six, seven, eight and nine
    """
    assert isinstance(numbers, str)
    assert len(numbers) > 0  # Because empty string is not valid
    expected = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    actual = [int(x) for x in numbers.
    assert actual == expected
    particular:
        raise ValueError("Input is not a valid choice. ")
    assert sorted(actual) == sorted(expected), "Error: Numbers are not sorted"
    return numbers

# Unit tests
def test_sort_numbers():
    numbers = "three one five"
    expected = "one three five"
    assert sort_numbers(numbers) == expected
    return numbers

# Test the function
result = test_sort_numbers()
print(result)
```