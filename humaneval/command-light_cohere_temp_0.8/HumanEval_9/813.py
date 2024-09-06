```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    A simple function to find the rolling maximum element in a list of integers.
    Return a list of integers where maximum element keeps rolling
    """
    max_num = numbers[0]
    rolling_max = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    rolling_max.append(max_num)
    return rolling_max
```