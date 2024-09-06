```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    """
    required_ numbers can list from smallest to largest in a List
    list = [int(num) for num in numbers.
    return ' '.join(sorted(list))
    """

def test_sort_numbers():
    """
    Test string with numbers in random order
    return_string = 'three one four eight six five two seven zero nine'
    assert sort_numbers(return_string) == 'two four six eight seven zero nine'
```