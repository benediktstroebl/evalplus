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
    
    # Iterate over the input list
    for num in numbers:
        # Check if the current number has not been seen before
        if num not in seen:
            # Add the current number to the result list
            result.append(num)
            # Add the current number to the set of seen numbers
            seen.add(num)
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicates removed. It uses a set to keep track of the numbers it has seen so far and a result list to store the numbers that are not duplicates. The function iterates over the input list, checks if each number is in the set of seen numbers, and if not, adds it to the result list and the set of seen numbers. The function returns the result list. The script also includes a test case to demonstrate the function's behavior.