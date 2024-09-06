```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests for the function
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4]

result = intersperse(numbers, delimiters)
print(result == [1, 4, 2, 4, 3, 5])  # This should print True
print(result == [1, 4, 9, 12])  # This should print False
```