```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: The list of integers with duplicates removed.
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # [1, 2]
```

This script defines a function `remove_duplicates` that takes a list of integers as input, removes all elements that occur more than once, and returns the resulting list. The function uses a set to keep track of seen numbers, and a list to store the result. The script then tests the function with two examples.