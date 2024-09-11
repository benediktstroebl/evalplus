```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of numbers.
        delimiter (int): Number to be inserted between every two consecutive elements.

    Returns:
        List[int]: List with delimiter inserted between every two consecutive elements.
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
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input. It iterates over the list, appending each number to the result list, and also appending the delimiter after each number except the last one. The function returns the resulting list.

The script also includes test cases to demonstrate the function's behavior.