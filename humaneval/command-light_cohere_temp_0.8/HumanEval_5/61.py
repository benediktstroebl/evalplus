```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Input: numbers -> List[int].
    Returns: List[int] with elements separated by 'delimiter'.
    """
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Test cases
print(inperse([1, 2, 3], ''))  # [1, 2, 3]
print(inperse([1, 2, 3, 4], ''))  # [1, 2, 3, 4]
print(inperse([1, 2, 3, 4, 5], ''))  # [1, 2, 3, 4, 5]
```