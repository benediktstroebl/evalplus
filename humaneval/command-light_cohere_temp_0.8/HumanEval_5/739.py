```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 8, 2, 12, 3, 16]

numbers = [1, 2, 3]
delimiters = [4]
result = intersperse(numbers, delimiters)
assert list(result) == [5, 9, 13]

numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8, 16]
result = intersperse(numbers, delimiters)
assert list(result) == [5, 20, 28, 12, 35]
```