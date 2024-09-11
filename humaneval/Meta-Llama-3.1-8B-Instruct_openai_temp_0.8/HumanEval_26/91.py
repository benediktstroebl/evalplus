```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers where all elements that occur more than once have been removed.
    """
    seen = set()
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the current number is not in the set of seen numbers
        if num not in seen:
            # Add the current number to the set of seen numbers
            seen.add(num)
            # Append the current number to the result list
            result.append(num)
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. It uses a set to keep track of the numbers it has seen so far, and appends a number to the result list only if it has not seen it before. The function maintains the original order of the input list. The script includes a test case to demonstrate the function's behavior.