```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once from the input list.
    Args:
        numbers: list of integers
    Returns: list of unique integers
    """
    seen = {}
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)
    return result
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers. The function uses a technique of maintaining a dictionary to track the seen numbers, and then appends the remaining numbers to the result list after checking if they have already been seen.