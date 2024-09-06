```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling max elements.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    result = [max(numbers[i:]) for i in range(len(numbers))]
    return result

>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
>>> rolling_max([10, 1, 2, 3])
[10, 3, 2]
>>> rolling_max([15, 16, 17])
[16, 17]
```
The function takes a list of integers as input and returns a list of rolling maximum elements found in the sequence. The function uses a efficient approach to store the previous maximum value and current index. The list comprehension approach is used to generate the list of rolling maximum elements.