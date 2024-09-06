```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3]
result2 = intersperse(numbers, 5)
assert list(result2) == [1, 5, 2, 5, 3]

# Test case 3
numbers = [10, 2, 3]
result3 = intersperse(numbers, 1)
assert list(result3) == [10, 1, 2, 3]
```