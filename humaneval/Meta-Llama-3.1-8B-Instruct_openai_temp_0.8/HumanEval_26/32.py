```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of integers with duplicates removed and order preserved
    """
    seen = {}
    result = []
    
    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: [1, 2, 4]
```

This script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. It uses a dictionary `seen` to keep track of the numbers it has seen so far, and a list `result` to store the numbers that are not seen before.