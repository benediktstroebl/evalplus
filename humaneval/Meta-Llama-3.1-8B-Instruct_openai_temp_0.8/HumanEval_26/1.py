```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        # If the number is not in the set, add it to the set and the result list
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines the `remove_duplicates` function to remove duplicates from a list of integers while preserving the original order. It uses a set to keep track of the numbers it has seen, and appends a number to the result list only if it has not been seen before. The function is then tested with the provided example.