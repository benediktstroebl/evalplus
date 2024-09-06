```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are strings can only numbers in the range [0,9].
    Returns the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    # mapping and checking valid input
    numbers = [int(num) for num in numbers.
    if all([num >= 0 and num <= 9]) and isinstance(numbers, List):
        return sorted(numbers)
    else:
        raise ValueError('Invalid input. If it is a list of numbers or contains non-numeric characters')
```