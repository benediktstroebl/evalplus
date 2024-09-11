```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): The list of numbers to intersperse.
        delimiter (int): The number to insert between every two consecutive elements.

    Returns:
        List[int]: The list with 'delimiter' inserted between every two consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if not the last element
            result.append(delimiter)
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```