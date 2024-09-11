```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between each pair of consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between each pair of consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # Expected output: [1, 0, 2, 0, 3, 0, 4, 0, 5]
print(intersperse([10, 20, 30, 40], 5))  # Expected output: [10, 5, 20, 5, 30, 5, 40]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and a delimiter `delimiter` as input. It iterates over the input list and appends each number to the result list, followed by the delimiter if it's not the last number in the list. The function returns the modified list.

The test cases at the end of the script verify that the function works correctly for different inputs.