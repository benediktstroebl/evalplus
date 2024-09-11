```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimeter (int): The number to be inserted between the elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []  # Base case: empty list, return empty list
    
    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.extend([delimeter, num])  # Insert delimeter and the current number
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script uses a simple and efficient approach to solve the problem. It starts with the first element of the input list and then iterates over the rest of the list, inserting the delimeter and the current number at each step.