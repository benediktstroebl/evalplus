```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed and original order preserved.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = dict()
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the seen dictionary, add it to the dictionary and the result list
        if num not in seen:
            seen[num] = True
            result.append(num)
    
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a dictionary to keep track of the numbers it has seen, and appends each number to the result list only if it has not been seen before. The function maintains the original order of the numbers in the input list.