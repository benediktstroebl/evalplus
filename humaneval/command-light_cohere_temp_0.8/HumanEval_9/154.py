```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, range(len(numbers)))][i]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```