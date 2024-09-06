```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from the list.
    Args:  numbers: List[int]
    Returns: List[int]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
```
This Python code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. 

The function uses a `set` data structure to keep track of elements that have been encountered before, and then iterates through the input list, adding elements to the `seen` set if they have not been seen before. Finally, the `result` list is populated with the unique elements from the input list.