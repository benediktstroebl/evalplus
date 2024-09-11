```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimeter (int): The number to be inserted as a delimiter.

    Returns:
        List[int]: The list with delimiters inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.extend([numbers[i - 1], delimeter])
    return result[:-1] if delimeter in result else result


# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This Python script defines the `intersperse` function that takes a list of integers and an integer delimiter as arguments, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. It includes docstrings and test cases to demonstrate its usage.