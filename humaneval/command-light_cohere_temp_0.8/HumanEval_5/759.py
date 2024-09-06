```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num+i*delimiter for i, num in enumerate(numbers)] + [delimiter]
# Tests
numbers = [1,2,3,4,5]
print(intersperse(numbers,4))  # [1,4,2,4,3,5,4]
```