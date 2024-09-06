```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'. Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', and 'nine'.
    Numbers are sorted in ascending order and returned as a string.
    """
    test cases:
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('two three four')
    'two three four'
    >>> sort_numbers('zero one two three')
    'zero one two three'
    >>> sort_numbers('Zero one two three')
    'zero one two three'
    >>> sort_numbers('zero E one two three')
    Traceback (most recent call last):
      File "<filename>", line 19, in <module>:
        sort_numbers('zero E one two three')
    ValueError: invalid literal for int() or str(): 'zero E one two three'
    """
    return numbers.sort()
[]
```