```python
from typing import List

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numbers from zero to nine.
    Valid choices are `zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine`.
    Returns the string with numbers sorted from smallest to largest
    """
    return numbers.split(' ',')[:-1].sort(numbers.split(' ',') + 1)
``` 
This script defines a function `sort_numbers` which sorts a given string of numbers in ascending order.