```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
assert len(result) == 6
assert all(map(lambda x: x % 2 == delimiters[0], result))  # 2, 6, 8
assert all(map(lambda x: x % 2 == delimiters[1], result))  # 1, 3, 5
print(result)
```