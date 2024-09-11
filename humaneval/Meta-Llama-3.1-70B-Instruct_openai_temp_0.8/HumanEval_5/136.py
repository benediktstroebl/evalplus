```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
        List[int]: The resulting list with 'delimiter' inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # Expected: []
print(intersperse([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as specified, and includes test cases to verify its correctness. The function iterates over the input list, appending each number and the delimiter (if it's not the last number) to the result list. The result is then returned.