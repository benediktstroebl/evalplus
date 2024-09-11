```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with the delimiter inserted.
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

This script defines a function `intersperse` that takes a list of integers and a delimiter integer as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a loop to iterate over the input list, appending each element to the result list, and also appending the delimiter if it's not the last element. The test cases at the end demonstrate the function's behavior.