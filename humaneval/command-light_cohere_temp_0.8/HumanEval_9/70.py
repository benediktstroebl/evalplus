```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns the list of rolling maximum elements in a given list.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4]
    """
    numbers.sort()
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return [max_num]
```