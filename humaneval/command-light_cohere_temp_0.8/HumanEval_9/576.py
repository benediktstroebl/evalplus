```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Args:
        numbers: list of integers
    Returns:
        list of integers
    """
    rolling_max_list = []
    for num in numbers:
        if num == rolling_max_list[-1]:
            rolling_max_list.append(num)
        else:
            rolling_max_list.append(num)
            rolling_max_max = num
    rolling_max_list.append(rolling_max_max)
    rolling_max_list.append(rolling_max_max)
    return rolling_max_list
``` 
Do you want any other code assistance?