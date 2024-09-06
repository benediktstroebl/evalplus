```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.max = max(numbers, key=lambda x: numbers[x] - x)
    return [max] + [numbers[i] - max for i, max in enumerate(numbers)]

# Test case
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```