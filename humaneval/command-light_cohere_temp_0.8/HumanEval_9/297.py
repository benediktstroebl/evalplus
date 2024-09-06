```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, _ in sorted((-n, n) for n in numbers)]

# Tests
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "List should have 7 elements"
assert all(result == [1, 2, 3, 3, 3, 4, 4])
assert all(map(max, result)) == [4, 3, 3, 4, 3, 4]
```