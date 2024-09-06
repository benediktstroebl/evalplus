```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]
# Tests
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7
assert all(result == [1, 2, 3, 3, 3, 4, 4])
```