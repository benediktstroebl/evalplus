```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove elements that occur more than once in a list.
    Args:
        numbers: list of integers
    Returns: list of integers, unique elements only
    """
    set(numbers)
    return list(set(numbers))
```

This script defines a function `remove_duplicates` that takes a list of integers as an argument and returns a new list with unique integer elements. The function uses the required Python set and list operations to achieve this.