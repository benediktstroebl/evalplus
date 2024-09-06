```python
from typing import List
def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are numbers: 
       zero, one, two, three, four, five, six, seven, eight, nine
    >>> sorted(numbers.split())
    string_arrr in ascending order
    """
    return numbers.split()
numbers.  # using the reason, numbers is a string, so we split it to convert it to a list
    numbers = [int(num) for num in numbers.split()]
    using a numbers in descending order, 
#         return ''.join numbers[::-1]
```