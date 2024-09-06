```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3]
delimiters = [4, 8]
expected = [5, 12, 16]

print("Result:", intersperse(numbers, delimiters))
print("Expected:", expected)
```