```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
    List[int]: The modified list with the delimeter inserted.
    
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example usage
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which iterates over the input list and inserts the delimeter between every two consecutive elements. The result is returned as a new list. The function is then tested with the provided example usage.