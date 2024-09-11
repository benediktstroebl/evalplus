```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = [numbers[0]]  # Start with the first element
    for i in range(1, len(numbers)):
        result.append(delimeter)  # Insert the delimeter
        result.append(numbers[i])  # Append the next number
    return result


# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function uses a simple loop to build the resulting list. The test cases at the end demonstrate the function's behavior with different inputs.