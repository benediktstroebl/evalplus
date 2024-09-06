```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num] + [num] + [delimiter] + [num] + [delimiter] + [num] + [delimiter] + [num]
    return result[:-1] + [next(numbers)]

# Test cases
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4]

print(intersperse(numbers, delimiters))  # Expected output: [1, 4, 2, 4, 3, 4, 5]
```