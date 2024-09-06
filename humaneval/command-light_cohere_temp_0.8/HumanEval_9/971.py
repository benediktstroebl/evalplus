```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers. RollingMax(numbers[0])  # Initializing the rolling index to 0
    rolling_maxes = [numbers[0]]
    for num in numbers[1:]:
        rolling_maxes.append(num)
        rolling_maxes.append(max(rolling_maxes[::1], num))
    return rolling_maxes
```