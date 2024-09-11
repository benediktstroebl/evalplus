```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: The input list of integers.
        delimiter: The integer to be inserted between list elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        # Insert delimiter before appending current number
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result


# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this code, we use a for loop with `enumerate` to iterate over the input list `numbers`. In each iteration, we append the current number to the result list and then append the delimiter if we're not at the last element in the list. This results in a list where the delimiter is inserted between every two consecutive elements of the input list.