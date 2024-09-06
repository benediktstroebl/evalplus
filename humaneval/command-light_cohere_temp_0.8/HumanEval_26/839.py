```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with elements left unchanged.
    """
   
    using sets to find duplicates and keeping only the first instance.
    """
    using a list comprehension to filter out non-unique items
    """
    # remove duplicates using sets and list comprehension
    unique = set(numbers)
    return [num for num in numbers if num not in unique]

# tests
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]
numbers = [3, 2, 4, 2, 5]
print(remove_duplicates(numbers))  # [2, 5]
```