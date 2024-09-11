```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): The input list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script creates a set `seen` to keep track of the numbers it has seen so far, and a list `result` to store the numbers without duplicates. It iterates over the input list, adding each number to `result` if it's not already in `seen`, and adding it to `seen` either way.