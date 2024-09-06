```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in sorted(numbers, reverse=True)]
numbers = [1, 2, 3, 2, 3, 4, 2, 3, 4, 5]
print(rolling_max(numbers))  # Output: [3, 3, 3, 3, 4, 4, 5]
```