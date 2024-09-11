```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`

    Args:
    numbers (List[int]): The input list of integers
    delimiter (int): The number to be inserted between elements

    Returns:
    List[int]: The list with delimiter inserted between every two consecutive elements

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])
    return result[:-1]  # remove the extra delimiter at the end


# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This code defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a simple loop to build the result list, and then removes the extra delimiter that is added at the end. The code also includes docstrings to describe the function's behavior and provide examples of usage.