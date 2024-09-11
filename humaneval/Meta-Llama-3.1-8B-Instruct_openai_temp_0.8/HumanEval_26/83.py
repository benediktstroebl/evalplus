```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with duplicates removed.

    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return list(dict.fromkeys(numbers))

# Example usage
numbers = [1, 2, 3, 2, 4, 5, 5, 6, 7, 8, 8, 9, 9]
print(remove_duplicates(numbers))
```

This script uses `dict.fromkeys()` to remove duplicate elements from the list while preserving the original order.