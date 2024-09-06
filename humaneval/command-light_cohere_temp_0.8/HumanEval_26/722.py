```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with elements left unchanged.
    """
Example usage:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This Python function, `remove_duplicates`, takes a list of integers as input and iterates through the list. It creates a set to track unique elements. For each number in the unique set, it adds the number to a new list. This process effectively removes duplicate elements and returns a list of unique integers.

The output of the function would be `[1, 3, 4]` in the given example.