```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: A new list with 'delimiter' inserted between consecutive elements.
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
```

This script defines the function `intersperse` that takes a list of numbers and a delimiter as input. It iterates over the input list and appends each number to the result list. If the current number is not the last element in the list, it also appends the delimiter to the result list. The function returns the result list.

The script includes two test cases to demonstrate the function's behavior.