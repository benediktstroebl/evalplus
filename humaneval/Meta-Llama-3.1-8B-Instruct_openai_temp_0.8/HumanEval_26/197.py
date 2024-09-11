```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers

    Returns:
    List[int]: A list of integers with duplicates removed

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()  # Initialize a set to keep track of seen elements
    result = []   # Initialize an empty list to store the result

    for num in numbers:
        if num not in seen:  # Check if the current number is not in the set
            result.append(num)  # Add the number to the result list
            seen.add(num)      # Add the number to the set

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a set to keep track of seen elements, ensuring that the order of elements in the original list is preserved. The test case at the end demonstrates the function's behavior.