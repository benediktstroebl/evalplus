```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are predefined list of numbers from lowest to highest.
    Convert input string to list of numbers
    Numbers are sorted in ascending order and returned as string.
    """
    validate_input(numbers)
    return numbers.sort()
```
def validate_input(numbers: str):
    """ Input must be a string of numbers separated by spaces """
    try:
        _ = [int(x) for x in numbers.}
        except:
            raise ValueError("Invalid input.
    return

def test_sort_numbers():
    """ Tests for sort_numbers function"""
    assert sort_numbers('three one five') == 'one three five'
    assert sort_numbers('zero nine') == 'zero nine'
    assert sort_numbers('9 8 7 6 5 4 3 2 1') == 'zero nine eight seven six five four three two'
    assert sort_numbers('5 4 3 2 1') == 'one four three two'
    assert sort_numbers('two three') == 'two three'
    assert sort_numbers('nine') == 'nine'
```