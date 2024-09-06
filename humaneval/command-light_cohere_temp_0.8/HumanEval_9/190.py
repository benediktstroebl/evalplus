```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers. Rolling_max(numbers) = sorted(numbers, reverse=True)
    return [x for x in rolling_max(numbers)]
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_res = rolling_max(numbers)
print(rolling_max_res)
```