```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): A number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The modified list with the delimiter inserted.
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

This Python script defines a function `intersperse` that takes a list of integers and a delimiter as input. It iterates over the input list, appending each number to the result list, and if it's not the last number in the list, it appends the delimiter as well. The function returns the modified list with the delimiter inserted. The script also includes test cases to verify the function's correctness.