```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimiter (int): Number to be inserted between consecutive elements.

    Returns:
        List[int]: List with 'delimiter' inserted between consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Don't append delimiter after last element
            result.append(delimiter)
    return result


# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

In this script, we iterate over the input list `numbers`. For each element, we append the element itself and the delimiter to the result list, but only append the delimiter if it's not the last element in the list. This approach ensures that the delimiter is inserted between every two consecutive elements.