```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers[1:]) if i < len(numbers) and numbers[i] > numbers[i - 1]]

# unit tests
numbers = [1, 2, 3, 4, 5]
print(rolling_max(numbers))  # [1, 2, 3, 3, 4]
```