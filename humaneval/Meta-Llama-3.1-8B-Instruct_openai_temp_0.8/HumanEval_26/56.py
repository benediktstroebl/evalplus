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
    seen = set()  # Keep track of the elements we've seen so far
    result = []  # Store the result here

    for num in numbers:
        if num not in seen:  # If we haven't seen this number before
            seen.add(num)   # Mark it as seen
            result.append(num)  # Add it to the result

    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with the same numbers, but with all duplicates removed. The function uses a `set` called `seen` to keep track of the numbers it has seen so far, and adds a number to the result list only if it's not already in the `seen` set. The function preserves the original order of the numbers.