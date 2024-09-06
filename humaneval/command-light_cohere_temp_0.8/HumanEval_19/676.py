```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers = [int(num) for num in numbers.
    return "".join(sorted(numbers))
```
The code defines a function `sort_numbers` that takes a string of numbers as input and returns the numbers sorted from smallest to largest. The function uses a list comprehension to convert the input string into a list of numbers, and then sorts this list using the `sorted` function. The sorted numbers are then joined together with spaces to form the sorted number string.