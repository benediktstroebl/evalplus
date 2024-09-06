```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(sorted(numbers))
    return [x for x in numbers if x > numbers[-1]]
# tests
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # expected output: [1, 2, 3, 3, 3, 4]
```