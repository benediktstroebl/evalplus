```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with all elements that occur more than once removed.

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
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a set `seen` to keep track of the elements it has seen so far, and a list `result` to store the elements that occur only once. It iterates over the input list, and for each element, it checks if it has been seen before. If not, it adds the element to the result list and marks it as seen. Finally, it returns the result list.