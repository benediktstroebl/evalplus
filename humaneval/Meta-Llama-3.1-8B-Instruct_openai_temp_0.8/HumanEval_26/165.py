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
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 4, 4, 5, 5, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
```

This script defines the `remove_duplicates` function, which takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a set to keep track of the elements it has seen so far, and appends each unique element to the result list. The script also includes a test case to demonstrate the function's behavior.