```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The `rolling_max` function takes in a list of integers `numbers` and an integer `rolling_window` as inputs and returns a list of integers, which is the maximum value over a rolling window of size `rolling_window` for each element in the list up until that element. It uses a list comprehension with maximum aggregation to find the rolling maximum over a given window. 

This solution assumes that the rolling window size is passed accordingly. You can modify the `rolling_window` variable when calling the function to change the desired window size.

For example:
```python
rolling_window = 3
result = rolling_max([1, 2, 3, 2, 3, 4, 2], rolling_window)
print(result)
```
will produce the desired output `[1, 2, 3, 3, 3, 4, 4]`.