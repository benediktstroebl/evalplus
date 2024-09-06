```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test case: Empty list
numbers = []
result = intersperse(numbers, 4)
assert len(result) == 0

# Test case: Basic list
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert len(result) == 6
assert result[0] == 1  # 1 4
assert result[1] == 5  # 1 4 2 4 3
assert result[-1] == 2  # 2 4

# Test case: Repeated values
numbers = [10, 10, 10]
result = intersperse(numbers, 4)
assert len(result) == 6
assert result[0] == 14  # 10 4 10 4
assert result[1] == 18  # 10 4 10 10
assert result[-2] == 12  # 12 4

# Test case: Different delimiter
numbers = [1, 2, 3]
result = intersperse(numbers, 10)
assert len(result) == 6
assert result[0] == 11  # 1 10
assert result[1] == 12  # 2 10 3

# Test case: Custom delimiter
numbers = [1, 2, 3]
result = intersperse(numbers, "" )
assert len(result) == 6
assert result[0] == 1  # 1
```