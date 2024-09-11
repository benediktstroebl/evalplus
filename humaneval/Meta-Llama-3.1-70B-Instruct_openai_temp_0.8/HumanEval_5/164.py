```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # check if it's not the last element
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]

# Or using list comprehension and itertools
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return list(itertools.chain(*zip(numbers, [delimiter] * len(numbers))))[:-1] if numbers else []

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```