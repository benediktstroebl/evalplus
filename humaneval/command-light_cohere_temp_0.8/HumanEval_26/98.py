```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate integers from the list.
    Returns a ** list of unique integers.
    """
   
    example:
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

This function, `remove_duplicates`, takes a list of integers as input and returns a new list containing only the unique elements. It achieves this by using a set to keep track of seen numbers and then iterates through the input list, adding elements to the set and to the result list if they are not already in the set.