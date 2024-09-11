Here's a self-contained Python script that solves the problem:

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
print(intersperse([10, 20, 30, 40], 5))  # Expected output: [10, 5, 20, 5, 30, 5, 40]
```

This script defines the `intersperse` function, which iterates through the input list `numbers`. For each number, it appends the number to the result list and then checks if it's not the last number in the list. If it's not the last number, it appends the `delimeter` to the result list. Finally, it returns the result list.

The script also includes test cases to demonstrate the function's behavior with different inputs.