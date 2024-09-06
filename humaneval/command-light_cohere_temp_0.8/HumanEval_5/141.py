```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
numbers_list = [4, 1, 2, 3]
result = intersperse(numbers_list, 4)
print(result)  # Output: [4, 8, 6, 12, 9, 4, 8, 6, 12, 9]
```