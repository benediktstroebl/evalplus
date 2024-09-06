```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(numbers, reverse=True)]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```