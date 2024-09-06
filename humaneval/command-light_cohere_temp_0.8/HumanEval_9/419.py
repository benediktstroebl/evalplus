```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of rolling max elements from the given list of integers.
    Each element in the time interval [0, n]
    will be replaced with the rolling max element.
    """

    List comprehension approach to select the max elements from the list.
"""
    return [n for n, x in enumerate(numbers):
        if n > len(numbers)//2:
            return x
        rolling_max = x
        for num in numbers[:n]:
            if num > rolling_max:
                rolling_max = num
        return [rolling_max]
```