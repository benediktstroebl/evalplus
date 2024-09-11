```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
    List[int]: The resulting list with the delimeter inserted

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimeter)
        result.append(num)
    return result[:-1]  # Remove the extra delimeter at the end

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements. It uses a simple iterative approach to build the resulting list. The function also includes a docstring with example usage and a check for the empty list case.