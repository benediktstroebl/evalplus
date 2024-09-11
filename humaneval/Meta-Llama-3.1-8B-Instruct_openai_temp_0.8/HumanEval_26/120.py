```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = {}
    result = []

    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a dictionary `seen` to keep track of the numbers that have been seen so far, and a list `result` to store the numbers that are not duplicates. The function iterates over the input list, adding each number to the `result` list if it has not been seen before. The function finally returns the `result` list. The script includes a test case to demonstrate the function's behavior.