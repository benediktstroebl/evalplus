```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.
   
    Example: Remove all occurrences of elements that are duplicated from the input list, and return a new list.
    """
    test:
   >>> numbers = [1, 2, 3, 2, 4]
   >>> remove_duplicates(numbers)
    [1, 3, 4]
    """
    seen = {}
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)
    finally, seen. imagine those values in the both in numbers that are not in the seen dictionary
    return result
```