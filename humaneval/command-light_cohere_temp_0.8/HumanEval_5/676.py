```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
   result.append(delimiter)
   return result
numbers = [1, 2, 3, 4, 5, 6]
print(intersperse(numbers, 2))  # Expected output: [1, 2, 3, 4, 5, 6]
```