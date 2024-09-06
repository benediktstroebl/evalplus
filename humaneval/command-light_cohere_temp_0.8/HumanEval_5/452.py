```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers: list of integers,
                 delimiter: positive integer, inserted between every 2 consecutive elements
    Returns:
        list of integers, with the delimiter between every 2 consecutive elements.
    """
    print(funsperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
    """
    return [i + delimiter for i, delimiter in enumerate(numbers, delimeter)]
```