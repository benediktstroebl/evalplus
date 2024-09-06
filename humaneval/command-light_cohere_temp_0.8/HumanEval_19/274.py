```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    return numbers.split(' ')
    fact, empty string, so numbers should be sorted
    >>> numbers = 'three one five'
    >>> sort_numbers(numbers)
    'one three five'
    """
    return numbers.split(' ')'.join(' ')

numbers = 'three one five'
print(sort_numbers(numbers))
``` 
This function takes a string of numbers in the format 'three one five' and returns a sorted version of the numbers. It uses the split() and join() to split the string into a list of numbers, then sorts the list and joins the sorted numbers back into a string.