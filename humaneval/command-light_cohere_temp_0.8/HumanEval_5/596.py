```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers[:2] + [delimiter] + numbers[2:]

# Test the function
numbers = [4, 2, 8, 3]
result = intersperse(numbers, 4)
assert len(result) == 6
assert list(result) == [1, 4, 2, 8, 3]
```