```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs and expected outputs
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print("Result:", result)

expected = [1, 4, 8, 12, 16, 20]
print("Expected:", expected)
```