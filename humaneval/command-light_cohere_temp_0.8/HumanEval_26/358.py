```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from the list of integers.
    Args: 
        numbers: list of integers.
    Returns: list with no duplicates.
    """
   
    list with all unique integers.
    """
Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [x for x in set(numbers) if numbers.count(x) == 1]
```