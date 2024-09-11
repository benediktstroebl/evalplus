```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between the elements of the input list.

    Returns:
        List[int]: The modified list with the delimeter inserted between every two consecutive elements.
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    return result


# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as specified in the problem statement, and also includes example usage to demonstrate how the function works.