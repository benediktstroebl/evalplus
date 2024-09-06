Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(zip(numbers, numbers[::-1]))[1]) for _ in range(len(numbers) - rolling_window + 1)]
```

The function takes in a list of numbers and an integer `rolling_window`. It uses a list comprehension to find the rolling maximum within consecutive windows of size `rolling_window`. The outer list comprehension iterates over each window, while the inner `zip` operation pairs each element with its corresponding element in the previous window. The `max` function is applied to these pairs, ensuring that the maximum element is selected for each window.