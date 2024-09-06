```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine,
    Valid choices are zero, one, two, three, four, five, six, seven, eight, and nine.
    numbers = list(numbers.split(' '))
    sort()
    return ''.join Numbers with invalid choices are removed from the string
    """
    numbers = list(numbers.split(' '))
    numbers = [num for num in numbers if num.isdigit()]
   
numbers. filter = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return ''.join numbers if len(numbers) < 10 else 'error'
```