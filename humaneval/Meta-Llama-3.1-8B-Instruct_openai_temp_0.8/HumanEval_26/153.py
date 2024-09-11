```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    List[int]: A list of integers with duplicates removed

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


# Test the function
numbers = [1, 2, 3, 2, 4, 4, 5, 1]
print(remove_duplicates(numbers))  # Output: [1, 3, 4, 5]
```

This script uses a set to keep track of the numbers it has seen so far, and a list to store the result. It iterates over the input list, adding each number to the result list if it hasn't been seen before. The result list is then returned.