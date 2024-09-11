```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
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

    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    
    # Remove the extra delimeter at the end if present
    if result and result[-1] == delimeter:
        result.pop()

    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2], 4))  # [1, 4, 2]
print(intersperse([1], 4))  # [1]
```

This script defines a function `intersperse` that takes a list of integers and an integer as arguments, and returns a new list with the specified integer inserted between every pair of consecutive elements. The function handles edge cases such as an empty input list and a list with a single element. The script includes test cases to demonstrate the function's behavior.