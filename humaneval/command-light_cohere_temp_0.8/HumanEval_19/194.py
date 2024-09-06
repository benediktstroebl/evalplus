```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split()
   e match number
        optional and non-digit and non-space
        all numbers will be transformed to floats and sorted in ascending order
    >>> sort_numbers('three one five')
    'one three five'
    >>> sort_numbers('  two three four')
    'two three four'
    >>> sort_numbers('abc123')
    'abc123'
    >>> sort_numbers('9')
    '9'
    """
    numbers = numbers.split()
    numbers = [n for n in numbers if n.isdigit()]
    Numbers = [float(n) for n in numbers]
    sorted_numbers = sorted(Numbers)
    return ''.join ''.join(sorted_numbers)
```