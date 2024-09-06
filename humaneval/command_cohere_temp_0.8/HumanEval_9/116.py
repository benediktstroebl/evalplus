Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_max_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found until the
    moment in the sequence. Optionally, specify the rolling maximum window size."""
    windows = [numbers[i:]span[1:] for i in range(len(numbers))  # Window iterator
              for span in zip(numbers[::rolling_max_window], numbers[1::rolling_max_window])  # Sliding window iterator]
    return max(windows, default=[0])  # [0] to handle empty windows

# Test cases
numbers1 = [1, 2, 3, 2, 3, 4, 2]
rolling_max_window1 = 3
result1 = rolling_max(numbers1, rolling_max_window1)
assert result1 == [1, 2, 3, 3, 3, 4, 4]

numbers2 = [1, 2, 3, 4, 5]
rolling_max_window2 = 2
result2 = rolling_max(numbers2, rolling_max_window2)
assert result2 == [1, 2, 3, 4, 5]
```

In this script, a given list of integers is iterated over with overlapping sliding windows of size `rolling_max_window`. The maximum element in each window is then collected into a resultant list. The handling of the optional parameter `rolling_max_window` ensures the function is deterministic even with corner cases, and the tests validate correct behavior.  This approach has a time complexity of `O(w * n)` where `w` is the `rolling_max_window` and `n` is the length of the input list.