```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit Tests
numbers = [1, 2, 3, 4]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
assert len(result) == 5
assert list(map(str, result)) == ['1 0 4', '2 4 8', '3 6 10', '4 12 16', '5 20 28']
```