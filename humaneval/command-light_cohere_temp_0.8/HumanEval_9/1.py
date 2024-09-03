```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements.
    >>> Returns a with positive numbers, the rolling maximum will keep the same value, 
    while negative numbers will have their own sign and roll.
    >>> rolling_max([1, 2, 3, -3, 4, -2, 5])
    [-2, -1, 4, 3, 2, 1]
    """
    max_index = 0
    result = []
    for i, num in enumerate(numbers):
        if num > numbers[max_index]:
            max_index = i
        result.append(num)
   return result
```