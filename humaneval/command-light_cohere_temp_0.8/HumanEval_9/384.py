```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates the maximum element that appears at least once during the given list.
    Args:
        numbers: list of integers.
    Returns: a list of integers with the maximum as the first element and 
        the rest as its decreasing order
    Returns:
        A list of integers, with the same ordering as the input list, but with the maximum element at the end.
    """
code"""
numbers = [1, 2, 3, 2, 3, 4, 2]
result = [num for num in numbers if num >= num[0]]
print(result)  # Output: [4, 3, 3, 4]
```