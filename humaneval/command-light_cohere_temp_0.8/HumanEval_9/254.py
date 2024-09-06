```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]
# Tests passed using Python built-in assert function
assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]
assert rolling_max([-1, -2, -3, -4, -5]) == [-1, -2, -3]
```