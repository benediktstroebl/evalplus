```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list.
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

This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set to keep track of elements that have been encountered before, and then iterates through the input list, adding elements to the set and the result list if they are not already in the set. Finally, the result list is returned.