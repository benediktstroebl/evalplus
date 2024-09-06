```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns a unique elements in a new list.
    """
    simple set(numbers)
    unique = set(numbers)
    return [x for x in numbers if x not in unique]
    return numbers
``` 
This code provides a self-contained function that takes a list of integers, removes all duplicate elements and returns the new list.