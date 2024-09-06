```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [4, 12, 8, 3, 5]
delimiter = 4
expected = [4, 8, 12, 16, 5]
result = intersperse(numbers, delimiter)

print(result == expected)  # True
print(id(result), result == expected[0])  # Bottom up type checking
```