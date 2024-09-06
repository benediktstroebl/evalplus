```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
numbers_list = [1, 2, 3]
result = intersperse(numbers_list, 4)
assert len(result) == 6
assert len([x for x in result if x != 4]) == 3
print(result)
```