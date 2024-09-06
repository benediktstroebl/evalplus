```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(sorted(numbers), range(len(numbers)))][i]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Expected output: [1, 2, 3, 3, 3, 3, 4, 4]
```