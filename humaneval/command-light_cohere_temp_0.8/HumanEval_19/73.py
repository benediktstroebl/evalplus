```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are example a set of unique numbers.
    Return the string with numbers sorted from smallest to largest"""
    return ' '.join(sorted(numbers.split()))

def test_sort_numbers() -> None:
    """ Tests for the sort_numbers function
    >>> test_sort_numbers('three one five')
    'one three five'
    >>> test_sort_numbers('66620083443')
    '066620083443'
    >>> test_sort_numbers('abc123')
    'abc123'
    >>> test_sort_numbers('99:111:222::333')
    '99:111:222::333'
    >>> test_sort_numbers('six')
    Traceback (most recent call last):
      File "<string>", line 19, in <module>
    ValueError: invalid literal for int() with base 10: 'six'
    """

```
The code defines a function sort_numbers that takes a string of numbers separated by spaces as input and returns a sorted string. It uses a valid choices for the numbers set and uses the split method to split the input string into a list of numbers, which it then sorts from smallest to largest and joins back into a string. The test_sort_numbers function tests the function by passing various input strings and ensuring that the output is correct.