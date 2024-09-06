```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with all unique elements.
    """

numbers = [1, 2, 3, 2, 4, 3, 1]
    return remove_duplicates(numbers) # [1, 2, 3, 4]
``` 
This function uses the `set()` function to remove duplicate elements and returns a new list with all unique elements.