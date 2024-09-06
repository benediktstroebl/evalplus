```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit Tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4, 2, 4, 3]
result = intersperse(numbers, delimiters)
shouldBe = [1, 4, 2, 4, 3, 5]

assert result == shouldBe
```