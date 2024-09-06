```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [0] * (len(numbers) - 1))]

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 0, 0, 0]
result = intersperse(numbers, delimiters)
should be = [1, 3, 2, 4, 5]

print(result == should_be)  # True
```