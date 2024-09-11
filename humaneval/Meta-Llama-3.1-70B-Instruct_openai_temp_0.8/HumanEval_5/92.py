```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements of `numbers'.

    Returns:
        List[int]: A new list with 'delimiter' inserted between every two consecutive elements of `numbers'.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Insert delimiter only if it's not the last element
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```