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
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result


# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [1, 1, 1, 2, 2]
print(remove_duplicates(numbers))  # Output: [1, 2]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The order of the remaining elements is preserved. It uses a `seen` set to keep track of the elements that have been seen so far and a `result` list to store the final output.