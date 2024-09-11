```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): The input list of integers.

    Returns:
    List[int]: The list with duplicates removed.

    Examples:
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

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a set `seen` to keep track of the elements it has seen so far, and a list `result` to store the elements that are not duplicates. It iterates over the input list, adding each element to the `result` list and the `seen` set if it has not been seen before. Finally, it returns the `result` list.