```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ 
    From a list of integers, remove all elements that occur more than once.
    Returns a a list of distinct integers.
    """
    list(set(numbers))
    """
    numbers = set(numbers)
    return list(numbers)

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
``` 
This script defines a function called `remove_duplicates` which takes a list of integers and returns a new list with no duplicates. The function achieves this using the set() and then converting it back to a list.