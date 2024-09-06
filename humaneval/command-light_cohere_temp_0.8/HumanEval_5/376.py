```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with different inputs
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)

print(result)  # Output: [1, 04, 2, 04, 3, 004, 4, 005]
```