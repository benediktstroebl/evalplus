```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between elements.
    
    Returns:
    List[int]: The list with 'delimeter' inserted between each pair of consecutive elements.
    
    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if we are not at the last element
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # Should print []
print(intersperse([1, 2, 3], 4))  # Should print [1, 4, 2, 4, 3]
```