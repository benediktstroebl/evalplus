Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[0]) for _ in range(len(numbers) - rolling_window + 1)]
```

The function `rolling_max` takes in a list of integers `numbers` and an integer `rolling_window` as input and returns a list of integers indicating the rolling maximum elements for a window of size `rolling_window` for each position in the sequence. The function achieves this by using the `max` function in a zip combined with range-based indexing to generate the appropriate list of rolling maximum values. 

This solution should correspond to the provided test case and others providing inputs as lists of integers.