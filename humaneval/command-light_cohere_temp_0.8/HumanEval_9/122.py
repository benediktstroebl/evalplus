```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in zip(numbers, numbers) if idx < len(numbers) and numbers[idx] > numbers[idx - 1]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # expected output: [1, 2, 3, 3, 3, 4, 4]
```