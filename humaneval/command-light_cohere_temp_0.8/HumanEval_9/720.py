```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, index in sorted((v, i) for i, v in enumerate(numbers)) if index < len(numbers) and numbers[index] > numbers[i]]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # [1, 2, 3, 3, 3, 4, 4]
```