```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Check if we're not at the last element in the list
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
print(intersperse([10], 4))  # [10]
```