```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
numbers = [4, 1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)
```