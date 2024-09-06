```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in sorted((num, i) for i, num in enumerate(numbers)) if i < len(numbers) and num > numbers[i]]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```