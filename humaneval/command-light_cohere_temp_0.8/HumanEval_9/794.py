```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [1, 2, 3, 2, 3, 4, 2]
    return [n for n, i in zip(numbers, numbers[1:])][::-1]
```