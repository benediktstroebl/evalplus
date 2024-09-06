```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in sorted((numbers), key=lambda x: x[1], reverse=True)]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```