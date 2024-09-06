```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3]
delimiters = [0, 4]

expected = [1, 4, 2, 4, 3]
result = intersperse(numbers, delimiters)

print(result == expected)
```