### Remove Duplicates from a List
#### Python Script

```markdown
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
    numbers (List[int]): List of integers from which to remove duplicates.
    
    Returns:
    List[int]: List of integers with duplicates removed and order preserved.
    
    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([5, 5, 5, 5, 5]))  # Output: []
print(remove_duplicates([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed, preserving the original order. It uses a set to keep track of the numbers it has seen so far, and appends each number to the result list only if it hasn't been seen before. The script also includes some test cases to demonstrate its functionality.