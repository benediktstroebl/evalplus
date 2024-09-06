```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes duplicate elements from a list of integers and returns a new list.
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
```
This script defines a function called `remove_duplicates` that takes a list of integers as input and removes duplicate elements from it, returning a new list. 

The function uses a set data structure to keep track of elements that have been seen before, and then iterates through the input list, adding elements to the result list if they are not already in the set. 

This implementation effectively removes duplicate elements from the input list.