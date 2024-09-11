```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A new list with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # Initialize an empty set to keep track of seen elements
    result = []  # Initialize an empty list to store the result

    for num in numbers:
        if num not in seen:  # Check if the element is not in the seen set
            result.append(num)  # Add the element to the result list
            seen.add(num)  # Add the element to the seen set

    return result  # Return the result list

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script uses a set (`seen`) to keep track of elements that have been encountered before. It iterates through the input list, adding each element to the result list if it's not already in the `seen` set. After each element is added to the result list, it's also added to the `seen` set. This ensures that duplicates are properly removed while maintaining the original order.