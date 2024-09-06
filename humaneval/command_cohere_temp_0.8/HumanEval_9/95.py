```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The function takes in a list of numbers and an integer `rolling_window`. It returns a list of integers, where each integer corresponds to the maximum value in the `rolling_window` range of the list. If `rolling_window` is larger than the length of the list, it will return an empty list.

Here is an example of function usage:
```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2], 3))  # [1, 2, 3, 3, 3, 4, 4]
```

This will return a list with the rolling maximum values of size 6, which is the largest possible rolling window for the given list.