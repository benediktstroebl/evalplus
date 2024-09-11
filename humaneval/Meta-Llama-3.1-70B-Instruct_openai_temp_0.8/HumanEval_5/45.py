```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): A delimiter number to be inserted.
    
    Returns:
        List[int]: A new list with delimiters inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([10, 20, 30, 40], 5))  # [10, 5, 20, 5, 30, 5, 40]
```

This script uses a simple iterative approach to insert the delimiter between every two consecutive elements in the input list. It appends each number from the input list to the result list, followed by the delimiter if it's not the last number in the list. The result is a new list with delimiters inserted as required.