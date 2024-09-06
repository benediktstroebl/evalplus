```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list with unique integers.
    """
example
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theunique list(result))
```