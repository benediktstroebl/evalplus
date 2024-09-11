```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result

# Example usage
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input, and returns a new list where `delimiter` is inserted between every two consecutive elements of `numbers`. The function uses a loop to iterate over `numbers`, appending `delimiter` before each element except the first one. The resulting list is then returned.