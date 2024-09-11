## Removing Duplicate Elements from a List
### Problem: Remove all elements from a list that occur more than once, preserving the original order.

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements from a list that occur more than once, preserving the original order.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with all elements that occur more than once removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # Initialize an empty set to keep track of seen elements
    result = []  # Initialize an empty list to store the result

    for num in numbers:  # Iterate over the input list
        if num not in seen:  # Check if the current element has been seen before
            seen.add(num)  # Add the current element to the set of seen elements
            result.append(num)  # Add the current element to the result list

    return result  # Return the result list


# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

This script uses a `set` to keep track of elements that have been seen before, allowing it to efficiently remove duplicates while preserving the original order.