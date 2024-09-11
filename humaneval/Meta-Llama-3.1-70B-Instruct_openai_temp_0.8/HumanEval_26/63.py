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
    """
    seen = set()
    seen_twice = set()

    for num in numbers:
        if num in seen:
            seen_twice.add(num)
        else:
            seen.add(num)

    return [num for num in numbers if num not in seen_twice]

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # []
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1, 1]))  # []
```

This script defines a function `remove_duplicates` that takes a list of integers as input, removes all elements that occur more than once, and returns the resulting list. The order of elements in the output list is the same as in the input list. The function uses two sets, `seen` and `seen_twice`, to keep track of the numbers it has seen so far and the numbers that have been seen twice, respectively. The function then uses a list comprehension to create the output list, including only the numbers that have not been seen twice.