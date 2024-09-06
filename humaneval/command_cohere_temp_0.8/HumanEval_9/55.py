```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [num for num in numbers]
    for idx, number in enumerate(numbers[1:]):
        if number > rolling_maxes[idx]:
            rolling_maxes[idx] = number
    return rolling_maxes
```

The algorithm uses a list `rolling_maxes` to store the maximum elements seen thus far and updates it iteratively, invoking a constant-time lookup on each element processing. This yields an efficient, linear time complexity of O(n) for the algorithm, represented by the line:
```python
rolling_maxes = [num for num in numbers]
for idx, number in enumerate(numbers[1:]):
    if number > rolling_maxes[idx]:
        rolling_maxes[idx] = number
```