```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are string must contain valid numbers, and be sorted from smallest to largest.
    >>> numbers = ['three one five', 'two three four']
    >>> sort_numbers(numbers)
    'one three four five'
    """
    numbers = [int(n) for n in numbers.
    return ' '.join(str(num) for num in sorted(numbers))

# Test cases
test_sort_numbers = """
def test_sort_numbers():
    return sort_numbers('three one five') == 'one three five'
"""

test_sort_numbers.py
```