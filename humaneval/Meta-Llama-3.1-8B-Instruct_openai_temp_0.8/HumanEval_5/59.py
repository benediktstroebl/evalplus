```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between each pair of consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted between each pair of consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimeter)
        result.append(numbers[i])
    return result


# Test the function
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input. The function inserts the `delimeter` between every two consecutive elements of the input list and returns the modified list. The script also includes test cases to demonstrate the function's behavior.