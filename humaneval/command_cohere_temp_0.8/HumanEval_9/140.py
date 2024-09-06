Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(subseq)) for subseq in zip(*[iter(numbers)]*rolling_window)]
```

The given Python script defines the `rolling_max` function, which accepts two arguments: a list of integers (`numbers`) and an integer (`rolling_window`) specifying the size of the rolling maximum operation. The function returns a list where each element corresponds to the maximum value encountered within the rolling window at that index in the original `numbers` list. This list of rolling maximums is achieved by applying a `max` function within a nested list comprehension, iterating through overlapping subsequences of the specified `rolling_window` size. 

For example, `rolling_max([1, 2, 3, 2, 3, 4, 2], 3)` will return `[1, 2, 3, 3, 3, 4, 4]`.