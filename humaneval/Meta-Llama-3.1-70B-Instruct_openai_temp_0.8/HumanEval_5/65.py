```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The list with the delimiter inserted between consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a loop to iterate over the input list, appending each element to the result list and appending the delimiter after each element except the last one. The example use cases demonstrate the function's behavior with an empty list and a non-empty list.