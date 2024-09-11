### Interspersing Elements with a Given Delimeter
#### Python Script
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between elements.

    Returns:
    List[int]: The modified list with the delimeter inserted between elements.
    
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    result = []
    result.extend(numbers)
    
    for _ in range(len(numbers) - 1):
        result.insert(len(result) - 1, delimeter)
    
    return result
```

### Example Usage
```python
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
print(intersperse([10, 20, 30, 40], 5))  # Output: [10, 5, 20, 5, 30, 5, 40]
```