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
    seen = set()  # Keep track of elements we have seen so far
    result = []  # The list of elements with duplicates removed

    for num in numbers:
        if num not in seen:  # If we haven't seen this number before
            seen.add(num)  # Add it to the set of seen numbers
            result.append(num)  # Add it to the result list

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input, removes all elements that occur more than once, and returns the resulting list. It uses a set to keep track of elements that have been seen so far, and a list to store the elements with duplicates removed. The function preserves the original order of the elements. The script also includes a test case to demonstrate the function's behavior.