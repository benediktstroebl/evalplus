```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(n) for n, index in zip(numbers, range(len(numbers))) if index % 2 == 0]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
assert [max(n) for n in numbers] == [rolling_max(numbers)], "Wrong output for basic test"

```