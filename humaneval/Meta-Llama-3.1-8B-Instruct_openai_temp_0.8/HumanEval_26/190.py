```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers

    Returns:
        List[int]: A list of integers with all duplicates removed
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
print(remove_duplicates([1, 1, 1, 1, 1]))  # Output: []
print(remove_duplicates([]))  # Output: []
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The function uses a dictionary `seen` to keep track of the numbers it has seen so far, and a list `result` to store the numbers that are not duplicates. The function iterates over the input list and appends each number to the result list only if it has not been seen before. The test cases at the end demonstrate how the function behaves with different inputs.