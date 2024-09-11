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
    seen = set()  # Create an empty set to store unique elements
    result = []  # Create an empty list to store the result
    for num in numbers:  # Iterate over the input list
        if num not in seen:  # Check if the current element is not in the set
            result.append(num)  # Add the current element to the result list
            seen.add(num)  # Add the current element to the set
    return result  # Return the result list


# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a list with no duplicates. It uses a set to keep track of unique elements and a list to store the result. The function iterates over the input list, checks if each element is in the set, and if not, adds it to the result list and the set. The result list is then returned. The script also includes a test case to demonstrate the function's usage.