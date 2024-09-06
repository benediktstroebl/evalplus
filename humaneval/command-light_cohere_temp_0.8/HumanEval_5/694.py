```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3, 4]
delimiters = [0, 4]  # Examples of the 'delimeter' to be inserted

result = intersperse(numbers, delimiters)
print("Result:", result)  # Expected output: [0, 4, 2, 4, 3, 8, 10]
```