```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The modified list with the delimeter inserted.

    Examples:
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
print(intersperse([-5, 0, 5], 0))  # [-5, 0, 0, 0, 0, 5]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter as input, inserts the delimeter between every two consecutive elements, and returns the modified list. The function uses a simple loop to iterate over the input list and append each number and the delimeter to the result list. If the current index is not the last index in the list, it appends the delimeter. The script also includes test cases to demonstrate the function's behavior.