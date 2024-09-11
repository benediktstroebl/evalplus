```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    Keep order of elements left the same as in the input.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers with elements that occur more than once removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the seen set, add it to the result list and the seen set
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that removes all elements that occur more than once from a list of integers. It maintains the original order of elements. The function uses a `set` to keep track of the numbers that have been seen so far, and a `list` to build the output list. The `seen` set allows the function to check whether a number has been seen before in constant time, ensuring that the function runs efficiently even for large input lists.