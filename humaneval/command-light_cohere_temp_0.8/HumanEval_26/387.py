```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate numbers from a list, returns a unique list.
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