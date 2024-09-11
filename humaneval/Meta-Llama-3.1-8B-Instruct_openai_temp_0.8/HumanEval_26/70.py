```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
    numbers: A list of integers
    
    Returns:
    A list of integers with duplicates removed
    
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
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]

numbers = [1, 1, 2, 2, 3, 3]
print(remove_duplicates(numbers))  # Output: [1, 2, 3]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set to keep track of the elements it has seen so far, and only adds an element to the result list if it hasn't been seen before. The order of the elements in the result list is the same as in the input list.