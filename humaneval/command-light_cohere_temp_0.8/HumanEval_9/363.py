```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in sorted((idx for idx, num in enumerate(numbers) if num > numbers[idx]), reverse=True)]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```