```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string must contain only digits from zero to nine.
    Return the string with the numbers sorted from smallest to largest.
    >>> sorted(List([1,3,5]))
    'one three five'
    """
    return numbers.split(' ', ')[::-1].split(' ', )
```
The function `sort_numbers` in the provided code takes a string of numbers as input and returns a string with the numbers sorted from smallest to largest. The function works by first splitting the input string into a list of space-separated numbers, then using slicing to reverse the order of the list and join the strings back together with spaces.