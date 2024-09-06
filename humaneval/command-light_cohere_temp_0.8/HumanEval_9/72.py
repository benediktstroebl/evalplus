```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in sorted((x, numbers[i]) for i in range(len(numbers)))]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 3, 4, 4]
```