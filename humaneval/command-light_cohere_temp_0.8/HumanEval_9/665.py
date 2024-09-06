```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, idx in sorted((num for num in numbers), reverse=True) if idx < numbers.__len__]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```