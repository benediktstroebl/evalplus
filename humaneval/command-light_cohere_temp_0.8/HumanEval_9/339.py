```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize result list with first element, which will be the maximum
    rolling_max_res = [numbers[0]]
    
    for num in numbers[1:]:
        # Update the result list with current number and its rolling maximum
        rolling_max_res.append(max(rolling_max_res[-1:], num))
    
    return rolling_max_res
```
The provided code defines a rolling_max function that generates a list of rolling maximum elements from a given list of integers. The function uses the max function to find the maximum element within the rolling_max_res list and updates it accordingly.