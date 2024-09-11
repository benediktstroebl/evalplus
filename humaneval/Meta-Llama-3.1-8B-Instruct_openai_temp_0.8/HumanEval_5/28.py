```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.

    Examples:
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
if __name__ == "__main__":
    print(intersperse([], 4))
    print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input. It iterates over the input list, appending each number to the result list and then appending the delimeter. Finally, it returns the result list.

The script includes two test cases: one for an empty list and one for a list with three elements.