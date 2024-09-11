```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
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
print(intersperse([5, 10, 15, 20], 0))  # [5, 0, 10, 0, 15, 0, 20]
```

This script first initializes an empty list `result`. Then, it iterates over the input list `numbers`. For each number, it appends the number to `result` and checks if it's not the last number in the list. If it's not the last number, it appends the `delimiter` to `result`. Finally, it returns `result`, which is the input list with the `delimiter` inserted between every two consecutive elements.