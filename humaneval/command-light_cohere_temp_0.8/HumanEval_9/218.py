```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in numbers if x == max(numbers, default=0)]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "The length of the result should be 7."
assert result == [1, 2, 3, 3, 3, 4, 4], "The result should be the list of rolling maximum elements."
```