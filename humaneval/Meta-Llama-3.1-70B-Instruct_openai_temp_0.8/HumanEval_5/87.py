```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between consecutive elements.
    
    Returns:
        List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
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
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input. It iterates over the list, appending each number and the delimiter (if not the last element) to the result list. The function returns the modified list. The test cases demonstrate the function's behavior with different inputs.