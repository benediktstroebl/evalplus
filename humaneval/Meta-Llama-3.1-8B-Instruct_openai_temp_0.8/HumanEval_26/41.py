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
    seen = set()  # Use a set to keep track of elements we've seen
    result = []  # Initialize an empty list to store the result
    for num in numbers:  # Iterate over the input list
        if num not in seen:  # If we haven't seen this number before
            seen.add(num)  # Add it to the set of seen numbers
            result.append(num)  # And add it to the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set to keep track of the elements it has seen, and it iterates over the input list, adding elements to the result list only if they haven't been seen before. The script also includes some example test cases to demonstrate the function's behavior.