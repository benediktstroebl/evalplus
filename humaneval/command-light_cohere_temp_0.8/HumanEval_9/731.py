```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, idx in sorted((num, idx) for idx, num in enumerate(numbers)), 0 <= idx < len(numbers)]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # [1, 2, 3, 3, 3, 4, 4]
```