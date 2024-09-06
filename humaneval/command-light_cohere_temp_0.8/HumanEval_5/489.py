```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter]*2)]

# Test case:
numbers = [1, 2, 3]
delimiters = [4, 4]
result = intersperse(numbers, delimiters)
print(result)  # Expected output: [1, 4, 2, 4, 3]
```