```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:])] + numbers[0]
numbers = [1, 2, 3]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]
```