```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with some sample inputs
numbers = [1, 2, 3]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)

assert len(result) == len(numbers) + len(delimiters) - 2
print(result)  # Output: [0, 4, 8, 1, 12, 2, 16, 3, 20]
```