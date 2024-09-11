```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: A list of integers.
        delimiter: An integer to be inserted between every two consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1], 4))  # [1]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a for loop to iterate over the input list, appending each element to the result list and inserting the delimiter before each element except the first one. The script also includes some test cases to demonstrate the function's behavior.