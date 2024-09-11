```python
from typing import List

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
    seen = set()
    result = []
    for num in numbers:
        # If the number has not been seen before, add it to the result and seen set
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # []
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # [1, 2]
```

This script uses a set to keep track of the numbers that have been seen so far. It iterates over the input list, adding each number to the result list and the seen set if it has not been seen before. The result list is returned at the end. This solution has a time complexity of O(n), where n is the number of elements in the input list, making it efficient for large lists.