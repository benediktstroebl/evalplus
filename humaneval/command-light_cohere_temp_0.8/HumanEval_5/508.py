```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs and assert output
numbers = [1, 2, 3]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
assert len(result) == 6
assert all(map(int, result)) == [1, 4, 8, 16, 32]
```