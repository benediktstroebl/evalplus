```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements found until a given moment 
    in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers.sort()
    max_num = numbers[0]
    rolling_max = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        rolling_max.append(max_num)
    rolling_max.append(num)
    return rolling_max
```