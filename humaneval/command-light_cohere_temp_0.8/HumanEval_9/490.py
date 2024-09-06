```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of the rolling maximum elements in the given list.
    """
    list of integers, n = len(numbers)
    rolling_maxes = [numbers[0]]
    for i in range(1, n):
        rolling_maxes.append(max(rolling_maxes[-1], numbers[i]))
    return rolling_maxes

# Test cases
numbers1 = [1, 2, 3]
numbers2 = [2, 3, 4, 5]

rolling_max_result1 = rolling_max(numbers1)
print("Rolling Maxes for numbers1:", rolling_max_result1)

rolling_max_result2 = rolling_max(numbers2)
print("Rolling Maxes for numbers2:", rolling_max_result2)
```
This script defines a function `rolling_max` that takes a list of integers as input and returns a list of the maximum elements after applying a rolling window algorithm. It also provides two test cases to demonstrate the function's usage.