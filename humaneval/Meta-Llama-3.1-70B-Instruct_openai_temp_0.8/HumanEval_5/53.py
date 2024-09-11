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
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list where the delimiter is inserted between every two consecutive elements. The function uses a simple loop to iterate over the input list, appending each number and the delimiter (if applicable) to the result list. The script also includes some test cases to demonstrate the function's behavior.