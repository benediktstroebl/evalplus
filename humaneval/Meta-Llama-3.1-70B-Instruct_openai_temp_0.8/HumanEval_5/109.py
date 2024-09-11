```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between elements.

    Returns:
    List[int]: A new list with the delimiter inserted between elements.
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

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. It uses a for loop to iterate over the input list, appending each number and the delimiter (if not at the last element) to the result list.

Note that I changed the variable name `delimeter` to `delimiter` to correct the spelling.