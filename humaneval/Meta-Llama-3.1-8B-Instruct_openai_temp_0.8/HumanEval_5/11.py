```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted between consecutive elements.

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

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the function `intersperse` that takes a list of integers and a delimiter as input. It then iterates over the list, appending each number and the delimiter (if not the last number) to the result list. The function returns this modified list. The script also includes test cases to demonstrate the function's behavior.