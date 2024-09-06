```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with unique elements.
    """
    removed duplicates"""
"""
    set(numbers) = {item for sublist in numbers for item in sublist if item not in set(sublist)}
    return list(set(numbers))
```
This function uses the set data structure to remove duplicate elements from the input list. It creates a set from the list of integers, then iterates through each item and checks if it's already in the set. Finally, the function returns the list of the elements that are not already in the set, effectively removing duplicates.