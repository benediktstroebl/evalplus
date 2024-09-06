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

This function takes a list of integers as input and returns a new list with all unique elements from the input. It utilizes a simple approach that uses a set to keep track of seen elements and creates a new list with all remaining elements.