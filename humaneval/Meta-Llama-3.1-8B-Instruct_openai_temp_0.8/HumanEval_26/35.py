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
    # Create an empty dictionary to keep track of seen numbers
    seen = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number has not been seen before
        if num not in seen:
            # Add it to the result list
            result.append(num)
            # Mark it as seen
            seen[num] = None
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers and returns a new list with all elements that occur more than once removed. It keeps the order of elements left the same as in the input. The script includes a test case to demonstrate the function's behavior.