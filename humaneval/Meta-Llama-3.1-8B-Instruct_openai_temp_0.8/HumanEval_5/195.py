```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.

    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between elements.

    Returns:
    List[int]: The list with the delimiter added between elements.

    Example:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input. It then iterates over the list, adding each number to the result list and then adding the delimiter. If it's not the last element in the list, it adds the delimiter after each number. The function returns the resulting list with the delimiter added between elements.