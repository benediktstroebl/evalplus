```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

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
print(intersperse([], 4))  # Expected: []
print(intersperse([1, 2, 3], 4))  # Expected: [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which iterates over the input list `numbers` and appends each number to the `result` list. If the current number is not the last one in the list, it also appends the `delimiter` to the `result` list. The function then returns the modified `result` list.

The script also includes two test cases to verify the correctness of the `intersperse` function.