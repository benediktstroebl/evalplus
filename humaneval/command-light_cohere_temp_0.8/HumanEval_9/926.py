```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, range(len(numbers))) if numbers[i] > numbers[(i + 1) % len(numbers)]]
```