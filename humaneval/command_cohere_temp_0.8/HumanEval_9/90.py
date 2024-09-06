```python
from typing import List, Tuple

def rolling_max(numbers: List[int], max_window: int = None) -> List[int]:
    if not numbers or max_window and max_window <= 0:
        return []

    if max_window:
        numbers, rolling_maxes = numbers[:max_window], []
    else:
        rolling_maxes = [float('-inf')] * len(numbers)

    for i in range(len(numbers)):
        max_val = max(rolling_maxes[i], numbers[i])
        rolling_maxes[i+1:] = [max_val] + [val for val in rolling_maxes[i+1:]]

    return rolling_maxes
```

The function takes an optional `max_window` parameter that determines the maximum size of the rolling window. By default, it iterates over the full list, calculating the rolling maximum. But you can set `max_window` to a specific value to limit the computation to the leading window of that size.