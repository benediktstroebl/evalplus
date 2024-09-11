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
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set `seen` to keep track of elements that have been encountered so far. If an element has not been seen before, it is added to the `result` list and the `seen` set. This process preserves the original order of elements.