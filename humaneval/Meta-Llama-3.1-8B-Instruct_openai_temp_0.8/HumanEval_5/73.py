```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The modified list with 'delimeter' inserted between elements.

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
        result.extend([delimeter, num])
    
    return result[:-1]  # Remove the extra delimiter at the end


# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that solves the problem. It first checks if the input list `numbers` is empty, in which case it returns an empty list. Otherwise, it initializes the result list with the first element of `numbers` and then iterates over the rest of the list. In each iteration, it appends the current number to the result list after inserting the `delimeter` between it and the previous number. Finally, it removes the extra delimiter at the end of the result list and returns it.