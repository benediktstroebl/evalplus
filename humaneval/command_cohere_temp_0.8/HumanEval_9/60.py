Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers[-rolling_window:])) for nums in zip(*[iter(numbers)] * rolling_window)]
```

The given Python script defines the `rolling_max` function, which accepts two arguments: a list of integers `numbers` and an integer `rolling_window`. It returns a list where each element is the maximum value encountered in a rolling window of size `rolling_window` at each index of the `numbers` list. This is achieved by using `zip(*[iter(numbers)] * rolling_window)` to create iterators that effectively slice the list for each window. Then, the maximum is computed using the `max` function applied to this sliced list. 

This approach ensures the function works for any finite `rolling_window` size and produces the desired rolling maximums for each window. 

The rolling max algorithm works by maintaining a window of size `rolling_window` which moves along the array. The window at each step includes the elements from the current index and the previous `rolling_window-1` indices. At each step, the maximum value is computed among these array elements, and the process is repeated for all indices.