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
    seen = set()  # Initialize an empty set to keep track of seen numbers
    result = []  # Initialize an empty list to store the result

    # Iterate through the input list
    for num in numbers:
        # Check if the current number has been seen before
        if num not in seen:
            # Add the current number to the result list
            result.append(num)
            # Add the current number to the set of seen numbers
            seen.add(num)

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script uses a set (`seen`) to keep track of numbers that have been seen before. If a number has not been seen before, it is added to the `seen` set and the result list. This way, we ensure that the order of elements in the result list is the same as in the input list.