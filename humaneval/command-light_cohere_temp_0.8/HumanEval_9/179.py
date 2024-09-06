```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A function to find the maximum element in a list,
    using rolling window approach.
    Returns a general case where max value is in the list or not.
    """
    list of integers
    """
    rolling_max_list = []
    for num in numbers:
        rolling_max_list.append(max(rolling_max_list[1:], num))
    return rolling_max_list
```