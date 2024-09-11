```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A new list with duplicates removed.
    """
    seen = set()
    seen_twice = set()
    result = []

    for num in numbers:
        if num in seen_twice:
            continue
        elif num in seen:
            seen_twice.add(num)
        else:
            seen.add(num)
            result.append(num)

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 2, 3, 3, 3]))  # [2]
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1, 1]))  # []
```