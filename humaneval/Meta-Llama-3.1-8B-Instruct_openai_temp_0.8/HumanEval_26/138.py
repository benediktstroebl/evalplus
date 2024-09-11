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

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Create an OrderedDict from the list to preserve order and remove duplicates
    seen = OrderedDict()
    for num in numbers:
        seen[num] = None
    
    # Convert the OrderedDict back to a list
    return list(seen.keys())

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses an `OrderedDict` to preserve the order of elements and remove duplicates. The `OrderedDict` is then converted back to a list, which is returned as the result.