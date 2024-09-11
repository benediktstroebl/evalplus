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
    if not numbers:  # If the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start with the first element
    
    for i in range(1, len(numbers)):  # Iterate over the rest of the list
        result.extend([delimeter, numbers[i]])  # Insert the delimeter and the current element
    
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines the `intersperse` function, which inserts a specified number `delimeter` between every two consecutive elements of the input list `numbers`. It then provides test cases to demonstrate the function's correctness.