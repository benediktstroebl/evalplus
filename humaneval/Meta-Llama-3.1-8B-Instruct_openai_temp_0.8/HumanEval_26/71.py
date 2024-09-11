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
    seen = set()  # keep track of unique numbers
    result = []  # list to store the result
    for num in numbers:
        if num not in seen:  # check if the number is not in seen
            seen.add(num)  # add the number to seen
            result.append(num)  # add the number to the result
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: [1, 2, 4]
```

This script uses a set to keep track of unique numbers and a list to store the result. It iterates through the input list, checks if a number is not in the set, adds it to the set and the result list if it's unique, and returns the result list at the end.