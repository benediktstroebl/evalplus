```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    Args:
        numbers (List[int]): A list of integers.
    Returns:
        List[int]: A list of integers with no duplicates and the original order preserved.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    unique_numbers = []
    
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    
    return unique_numbers


# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set `seen` to keep track of the numbers it has encountered so far. If a number is not in `seen`, it adds it to `seen` and to the result list `unique_numbers`. This way, the function preserves the original order of the numbers in the input list. The script also includes a test case to demonstrate the function's correctness.