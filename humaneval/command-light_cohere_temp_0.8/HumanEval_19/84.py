```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are return the unsorted numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.split(' ') '.join(sorted(numbers.split(' ')[::-1]))
```