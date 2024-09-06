```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers.
    Valid choices are numbers are 'zero' to 'nine', each with optional hyphens.
    Returns the  a string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = numbers.split(' ')')
    strings = [str.strip() for str in numbers]
    numbers.sort()
    simplest = ''three one five' 
    return ' '.join(strings) + '\n' + ''.join(numbers)
  ```