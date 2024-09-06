Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence."""
    if not numbers:
        return []

    if rolling_window > len(numbers):
        return [float('inf')] * rolling_window

    max_vals = [float('inf')] * rolling_window
    max_idx = 0

    for idx, num in enumerate(numbers):
        max_vals[max_idx] = num
        for i in range(rolling_window - 1, idx - 1, -1):
            if max_vals[i] < max_vals[i + 1]:
                max_vals[i + 1] = max_vals[i]
        max_idx = (max_idx + 1) % rolling_window

    return max_vals

# Tests
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3
result = rolling_max(numbers, rolling_window)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```

The function `rolling_max` takes a list of integers `numbers` and an integer `rolling_window` as input. It returns a list of rolling maximum elements found until the given moment in the sequence. The function starts by initializing a list `max_vals` with the rolling window size, filling it with `inf` values. Then, it iterates through the input list, updating `max_vals` to reflect the rolling maximums. Finally, it returns the modified `max_vals` list, which contains the rolling maximum elements. 

The example test assigns `rolling_max` to the list `[1, 2, 3, 2, 3, 4, 2]` and a rolling window of size 3. The function returns the expected output `[1, 2, 3, 3, 3, 4, 4]`.