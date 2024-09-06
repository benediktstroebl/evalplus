```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with sample inputs and expected outputs
numbers = [1, 2, 3]
delimiters = 4

expected = [1, 5, 7, 9]

result = intersperse(numbers, delimiters)
assert len(result) == len(expected)

print(result == expected)
```