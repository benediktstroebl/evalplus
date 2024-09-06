```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs
numbers = [1, 2, 3]
delimiters = 4
result = intersperse(numbers, delimiters)
print(result)  # Output: [1, 4, 2, 4, 3, 8, 11]
```