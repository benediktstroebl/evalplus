```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The list of integers to be modified.
    delimeter (int): The number to be inserted between elements.

    Returns:
    List[int]: The list with the delimeter inserted.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # check if not the last element
            result.append(delimeter)
    return result


# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines the `intersperse` function to insert the delimeter between elements in the input list. The `enumerate` function is used to get both the index and value of each element in the list. The delimeter is appended after each element, except for the last one, to avoid an extra delimeter at the end of the list.