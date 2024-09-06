```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3, 4, 5]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)
```