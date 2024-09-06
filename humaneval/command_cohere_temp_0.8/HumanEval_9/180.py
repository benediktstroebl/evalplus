Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(numbers)[i-rolling_window:i+1]) for i in range(len(numbers))]
```

The function rolling_max takes in a list of numbers and a rolling window size as input, and returns a list of the maximum elements from the rolling window at each position in the sequence. It uses a list comprehension to find the maximum element in the window over the entire list. To ensure consistency with the problem statement, I assume the rolling window size to be present in the rolling_window parameter and return a list of integers corresponding to the maximum elements at each position in the sequence.