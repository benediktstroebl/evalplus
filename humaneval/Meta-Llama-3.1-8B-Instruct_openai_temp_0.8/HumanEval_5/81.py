```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): A list of integers
        delimeter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: A list with the delimeter inserted between consecutive elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a number to be used as a delimeter. It iterates over the input list, appending each number to the result list followed by the delimeter if it's not the last element in the list. The test cases at the end demonstrate the function's behavior with an empty list and a list with three elements.