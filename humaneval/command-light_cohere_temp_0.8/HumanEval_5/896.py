```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with various inputs
numbers = [3, 1, 4]
delimiters = [2, 3]
result = intersperse(numbers, delimiters)
assert len(result) == 6
assert all(result == [3, 4, 1, 4, 3, 2])
```