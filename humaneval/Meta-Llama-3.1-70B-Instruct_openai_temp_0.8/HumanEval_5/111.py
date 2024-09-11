```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimiter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The resulting list with the delimiter inserted
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Insert delimiter after each number except the last one
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example use cases:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input. It iterates over the input list, appending each number to the result list, and then appending the delimiter after each number except the last one. The function returns the resulting list with the delimiter inserted between every two consecutive elements. The script also includes example use cases to demonstrate the function's behavior.