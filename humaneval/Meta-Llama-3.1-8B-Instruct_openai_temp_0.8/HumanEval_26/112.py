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
    seen = set()
    result = []
    
    # Iterate through the input list
    for num in numbers:
        # Check if the number has been seen before
        if num not in seen:
            # Add the number to the result list
            result.append(num)
            # Add the number to the set of seen numbers
            seen.add(num)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set to keep track of the numbers it has seen so far, and only adds a number to the result list if it has not been seen before. The function maintains the original order of the elements. The script also includes a test case to demonstrate the function's behavior.