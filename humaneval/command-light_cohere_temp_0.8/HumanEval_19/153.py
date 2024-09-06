```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are same integers
    >>> sort_numbers('three one five')
    'one three five'
    """
    return numbers.split(' ') '.join(sorted(numbers.split(' ')))

numbers = ['three', 'one', 'five']
print(sort_numbers(numbers))  # Output: 'one threefive'
``` 
The code defines a function **`sort_numbers`** that takes a string of numbers as input. The string is split into a list of numbers, and then these numbers are sorted from smallest to largest using the built-in Python function **`sorted`**. The sorted numbers are then joined back into the original string format.