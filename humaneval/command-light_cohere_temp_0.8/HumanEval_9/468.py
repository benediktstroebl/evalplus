```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers. max(:List(numbers)
    return [x for x in numbers if x == max(numbers, default=0)])

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7
assert result[0] == 1
assert result[1] == 2
assert result[2] == 3
assert result[3] == 3
assert result[4] == 4
assert result[5] == 3
assert result[6] == 4
assert result[7] == 4
```