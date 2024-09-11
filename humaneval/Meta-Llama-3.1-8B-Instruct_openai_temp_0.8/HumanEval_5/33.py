```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): Input list of integers
        delimiter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with the delimiter inserted

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    result = [numbers[0]]
    for i in range(len(numbers) - 1):
        result.append(delimiter)
        result.append(numbers[i + 1])
    return result


# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a simple iterative approach to construct the resulting list. The test cases at the end demonstrate the function's behavior.