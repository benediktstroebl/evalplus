```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] 

# Test case 1:
numbers = []
result = intersperse(numbers, 4)
assert len(result) == len(numbers)
assert all(isinstance(i, int) for i in result)

# Test case 2:
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
assert len(result) == len(numbers)
assert all(isinstance(i, int) for i in result)

# Test case 3:
numbers = [1, 2, 3, 4]
result = intersperse(numbers, 4)
assert len(result) == len(numbers)
assert all(isinstance(i, int) for i in result)
```