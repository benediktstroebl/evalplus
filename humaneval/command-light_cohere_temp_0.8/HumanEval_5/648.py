```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3]
delimiters = [4,]
result = intersperse(numbers, delimiters)
assert len(result) == 6
assert all(num >= 0 for num in result)
```