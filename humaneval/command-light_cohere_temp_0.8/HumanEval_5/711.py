```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3]
delimiters = [0, 4]

result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3]
result = intersperse([1, 2, 3], [0, 4])
assert list(result) == [1, 0, 2, 4, 3]

# Any other combinations or tests, and this function is self-contained!
```