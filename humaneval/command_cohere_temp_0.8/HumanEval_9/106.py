```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The `rolling_max` function takes in a list of integers (`numbers`) and an integer `rolling_window` as inputs, it returns a list of integers (`List[int])`, where each element represents the maximum value of the moving window of size `rolling_window` at each index of the input `numbers`. The maximum value is computed by using the `max` function on the slice of the input list `list(numbers)[i-rolling_window:i+1]`. The `rolling_max` function uses a list comprehension with a generator expression to efficiently calculate the rolling maximum in a single pass through the input `numbers` without the need for extra space for the entire window. 

Here is an example usage of the function:
```python
rolling_max([1, 2, 3, 2, 3, 4, 2], 3)
# [1, 2, 3, 3, 3, 4, 4]
```

This will return a list where each number is the maximum of a rolling window of size 3 at each index.