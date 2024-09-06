```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum elements found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([4, 5, 6])
    [6]
    >>> rolling_max([1, 2, 3, 4, 5, 6])
    [6]
    """
    max_roll = numbers[0]
    rolling_max_list = [max_roll]
    for num in numbers[1:]:
        current_max = max(max_roll, num)
        max_roll = current_max
        rolling_max_list.append(current_max)
    return rolling_max_list

```

This script defines a function called `rolling_max` which accepts a list of integers as an argument and returns a new list that contains the rolling maximum elements. The script uses the method `max` and loops through the list to find the rolling maximum element. The output of the list is the list of rolling maximum elements.