```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, idx in zip(numbers, range(len(numbers))) if numbers[idx] > numbers[idx - 1]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```