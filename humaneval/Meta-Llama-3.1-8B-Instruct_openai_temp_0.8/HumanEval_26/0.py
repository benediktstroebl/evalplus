```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): The list of integers from which to remove duplicates.

    Returns:
        List[int]: The list of integers with duplicates removed.

    Examples:
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


# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. It uses a set `seen` to keep track of the numbers that have appeared in the input list, and a list `result` to store the numbers that appear only once. The function iterates over the input list, adding each number to the result list if it has not been seen before. The example usage at the end demonstrates how to use the function to remove duplicates from a list of integers.