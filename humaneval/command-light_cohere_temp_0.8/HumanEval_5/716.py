```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimiter in zip(numbers, [delimeter] * 2)]

# Test cases
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]

expected = [1, 4, 8, 2, 12, 3, 16, 5]

print(f"Result: {expected}")
```