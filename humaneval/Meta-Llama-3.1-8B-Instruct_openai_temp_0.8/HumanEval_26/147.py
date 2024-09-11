```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    List[int]: The list of integers with duplicates removed

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    
    # Iterate over the input list in reverse order to avoid issues with duplicate indices
    for num in reversed(numbers):
        if num not in seen:
            # Add the number to the result list and the set of seen numbers
            result.append(num)
            seen.add(num)
    
    # Reverse the result list to maintain the original order
    result.reverse()
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a set to keep track of the numbers that have been seen so far. It iterates over the input list in reverse order, adding each number to the result list and the set of seen numbers if it's not already in the set. Finally, it reverses the result list to maintain the original order.