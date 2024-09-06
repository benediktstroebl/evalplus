```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    From a list of integers, remove all elements that occur more than once.
    Returns a  List[int] containing unique elements.
    """
input: List[int]
    """
    numbers = set(numbers)
    return list(numbers)
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The set function is used to remove duplicates, and the list is then converted back to a list using the `list` function.