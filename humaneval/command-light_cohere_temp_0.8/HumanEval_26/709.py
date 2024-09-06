```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from the input list.
    Args:
    numbers: List[int]

    Returns:
    List[int]: Unique list of integers
    """
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()]]
 set()
```

This code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicate elements removed. The `seen` set keeps track of elements that have been encountered before. The `for` loop iterates through the input list, and the element is only added to the `seen` set if it is not already in the `numbers` list or has been seen before.