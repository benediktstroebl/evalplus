```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimeter (int): A number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # If the list is empty, return it as is
    result = [numbers[0]]  # Start with the first element
    for i in range(1, len(numbers)):
        result += [delimeter, numbers[i]]  # Add delimeter and next number
    return result


# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers and a delimeter integer as input. It then returns a new list with the delimeter inserted between every two consecutive elements. The script also includes docstrings and test cases to demonstrate the function's usage.