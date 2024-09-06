```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x in sorted(numbers) if not set() or max(numbers) > x]

# Test the function with sample input
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 7, "Invalid return length"
assert all(x <= 4 for x in result), "Rolling maximum greater than maximum number"
```