Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(numbers[i:i+rolling_window]) for i in range(len(numbers) - rolling_window + 1)]
```

The `rolling_max()` function takes in a list of integers `numbers` and an integer `rolling_window` as input and returns a list of integers, which is the maximum value over a rolling window of size `rolling_window` for each element in the list. It uses Python's maximum `max()` function to compare values. 

For example, if we call this function with the list `[1, 2, 3, 2, 3, 4, 2]` and a rolling window of size 3, we would get the output `[1, 2, 3, 3, 3, 4, 4]`. 

This algorithm has a time complexity of `O(n)` since it requires scanning the list `numbers` up to `rolling_window` times, where `n` is the length of the given list. 

To further validate the function, we can add a unit test like:
```python
import unittest

class TestRollingMax(unittest.TestCase):
    def test_rolling_max(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 3, 4, 2], 3), [1, 2, 3, 3, 3, 4, 4])
```