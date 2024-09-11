```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between elements.

    Returns:
        List[int]: The resulting list with the delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimeter)
        result.append(num)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input, and returns a new list with the `delimeter` inserted between every two consecutive elements of `numbers`. The function uses a simple loop to iterate over the input list, appending the `delimeter` before each element except the first one. The test cases at the end demonstrate the function's behavior with an empty list and a non-empty list.