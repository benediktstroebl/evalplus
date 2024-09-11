```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): Number to be inserted between every two consecutive elements

    Returns:
        List[int]: List with 'delimeter' inserted between every two consecutive elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Insert delimeter after each number except the last one
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This script defines the `intersperse` function that inserts a given delimeter between every two consecutive elements of the input list. It uses a simple iterative approach to build the resulting list. The function includes type hints, a docstring, and example usage to demonstrate its behavior.