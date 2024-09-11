```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # If input list is empty, return it as is

    result = [numbers[0]]  # Start with the first element
    for i in range(1, len(numbers)):
        result.append(delimeter)  # Insert delimeter
        result.append(numbers[i])  # Append the next element

    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer `delimeter` as input. It inserts the `delimeter` between every two consecutive elements of the input list and returns the modified list. The function also includes test cases to demonstrate its usage.