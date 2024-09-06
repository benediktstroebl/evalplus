```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: unique elements, ordered as in the input.
    """
    List[set() does not sort the input list, so we use the order() method to return the input list ordered"""
    return [x for x in numbers if set(numbers).order()).remove(numbers) == set()]```

This code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list of integers, where all duplicate elements have been removed. The set() function is used to remove duplicate elements, and the `order()` method is used to return the elements in the original order.