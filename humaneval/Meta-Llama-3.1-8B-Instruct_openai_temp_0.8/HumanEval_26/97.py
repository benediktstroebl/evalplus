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
    
    # Iterate over each number in the list
    for num in numbers:
        # If the number has not been seen before, add it to the result and mark it as seen
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed, while preserving the original order. It uses a set `seen` to keep track of the numbers that have been seen so far, and appends a number to the result list only if it has not been seen before. The function is tested with an example list `[1, 2, 3, 2, 4]`, which yields the expected output `[1, 3, 4]`.