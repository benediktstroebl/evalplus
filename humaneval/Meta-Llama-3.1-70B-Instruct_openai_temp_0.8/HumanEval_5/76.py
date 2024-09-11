```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Don't append the delimiter after the last number
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input. It iterates over the input list, appending each number and the delimiter (if it's not the last number) to the result list. The function returns the modified list. The example usage at the end demonstrates the function's behavior with the provided test cases.