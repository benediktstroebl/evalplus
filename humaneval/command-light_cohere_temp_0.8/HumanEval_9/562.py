```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(numbers)]

# Test case 1: Basic test for function
numbers = [1, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result) == 6, "Result list should have 6 elements"
assert sorted(result) == [1, 2, 3, 3, 3, 4]

# Test case 2: Test case from the docstring
numbers = [1, 2, 3, 3, 4, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result) == 7, "Result list should have 7 elements"
assert sorted(result) == [1, 2, 3, 3, 4, 4, 5]
```