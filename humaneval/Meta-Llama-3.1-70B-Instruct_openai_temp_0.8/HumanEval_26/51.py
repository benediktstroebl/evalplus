```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The input list with all duplicates removed.
    """
    seen = set()
    duplicates = set()
    result = []

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
            result.append(num)

    # Remove elements that occur more than once
    result = [num for num in result if num not in duplicates]

    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all duplicates removed. The function uses two sets, `seen` and `duplicates`, to keep track of the numbers it has seen so far and the numbers that occur more than once, respectively. The function then uses a list comprehension to create a new list that excludes all duplicates.