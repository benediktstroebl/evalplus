```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, idx in sorted((num, idx) for idx, num in enumerate(numbers)) if num > numbers[idx] or idx == len(numbers) - 1]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```