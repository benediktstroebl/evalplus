```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.List = [sorted(numbers)]
    rolling_maxes = []
    for i in range(len(numbers)):
        while len(rolling_maxes) > 0 and numbers[i] < rolling_maxes[-1]:
            rolling_maxes.append(rolling_maxes[-1])
        rolling_maxes.append(numbers[i])
        rolling_maxes.return max = max(rolling_maxes, key=numbers.return max, 0)
    return rolling_maxes
```