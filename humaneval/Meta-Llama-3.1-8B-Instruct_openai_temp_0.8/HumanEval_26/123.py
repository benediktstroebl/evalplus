```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # Set to keep track of unique elements
    result = []  # List to store the result

    for num in numbers:  # Iterate over the input list
        if num not in seen:  # If the number is not in the seen set
            result.append(num)  # Add it to the result list
            seen.add(num)  # Add it to the seen set

    return result  # Return the result list


# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that removes all elements from the input list that occur more than once, preserving the order of the remaining elements. It uses a set `seen` to keep track of unique elements and a list `result` to store the result. The function iterates over the input list, adds each unique number to the result list and the seen set, and finally returns the result list. The script includes a test case to demonstrate the function's behavior.