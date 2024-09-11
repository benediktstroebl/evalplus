```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with no duplicates.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()  # Set to keep track of seen elements
    result = []  # List to store the result

    for num in numbers:
        # If the element is not in the seen set, add it to the seen set and result list
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines the `remove_duplicates` function and provides a test case to demonstrate its usage. The function iterates through the input list, adding each element to the result list only if it has not been seen before. The result list is then returned.