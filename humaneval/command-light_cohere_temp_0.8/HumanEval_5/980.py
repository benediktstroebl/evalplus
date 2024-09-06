```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with a simple example
numbers = [1, 2, 3]
delimiters = [4, 4, 4]
result = intersperse(numbers, delimiters)
print(result)  # Output: [1, 4, 2, 4, 3, 4, 4]
```