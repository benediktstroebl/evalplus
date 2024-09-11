```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed.
    """
    seen = set()
    duplicates = set()
    result = []

    # First pass: find duplicates
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)

    # Second pass: build result list
    for num in numbers:
        if num not in duplicates:
            result.append(num)

    return result

# Test cases
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 1, 2, 3, 3]))  # [2]
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([]))  # []
```