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
        # If the number is not in the seen set, add it to the result list and the set
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
```

In this script, we define a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses a set to keep track of the elements it has seen so far, and a list to build the result. It iterates over the input list, adding each element to the result list and the set if it hasn't been seen before. Finally, it returns the result list.