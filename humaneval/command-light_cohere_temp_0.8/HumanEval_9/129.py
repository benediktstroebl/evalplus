```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, n in zip(numbers, numbers) if n > x or not numbers[n]]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```