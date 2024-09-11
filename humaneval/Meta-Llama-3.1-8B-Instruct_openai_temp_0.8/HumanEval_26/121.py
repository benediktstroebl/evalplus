```python
from collections import OrderedDict
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of integers with duplicates removed
    """
    # Create an OrderedDict from the list, which automatically removes duplicates
    ordered_dict = OrderedDict((x, True) for x in numbers)
    # Return a list of the keys in the OrderedDict
    return list(ordered_dict.keys())

# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]
```

This script uses an `OrderedDict` from the `collections` module to remove duplicates from the list while preserving the original order. It then returns a list of the keys from the `OrderedDict`, which are the unique elements from the input list.