```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to insert between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if there's a next element
            result.append(delimiter)
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script uses a simple loop to iterate over the input list, appending each number to the result list and then appending the delimiter if there's a next element. This way, the delimiter is inserted between every two consecutive elements as required. The test cases at the end verify that the function works correctly for the given examples.