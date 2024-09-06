```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeterLen in zip(numbers, [delimeter for _ in range(len(numbers))])]

# Test the function
numbers = [1, 2, 3]
print(inpersepe(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]
```