```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes elements that occur more than once from a list of integers.
    return: A new list with all unique integers
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return: result
    return result
```