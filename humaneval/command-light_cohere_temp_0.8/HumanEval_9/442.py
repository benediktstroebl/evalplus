```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers) if x == max(numbers)]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 2, 1]
assert rolling_max(numbers) == [5]

numbers = [5, 2, 1, 6]
assert rolling_max(numbers) == [5]

numbers = [10, 20, 30]
assert rolling_max(numbers) == [20]

numbers = [1, 2, 3]
assert not rolling_max(numbers)
```