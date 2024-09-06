```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers[1:])] + [numbers[0]]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # expected output: [1, 2, 3, 3, 3, 3, 4, 4]
```