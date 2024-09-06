```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A simple function that calculates the rolling maximum element in a given list of integers.
    Parameters: numbers - list of integers
    Returns: list of integers, the rolling maximum elements found until the given moment.
    """
    list of integers with the maximum value as the last element, and the list is sorted in-place
    """
    numbers.sort()
    max_num = numbers[-1]
    rolling_max = [max_num]
    for num in numbers[:-(-1)] : 
        if num > max_num:
            max_num = num
        rolling_max.append(max_num)
    rolling_max.append(num)
    return rolling_max
```