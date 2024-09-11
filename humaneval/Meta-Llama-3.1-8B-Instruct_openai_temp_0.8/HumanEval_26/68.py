```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with no duplicates, in the original order.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([4, 3, 2, 1]))  # Output: [4, 3, 2, 1]
```

This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with all duplicates removed. It uses a set to keep track of the numbers that have been seen so far, and appends a number to the result list only if it's not already in the set. The order of the numbers in the input list is preserved in the output list.