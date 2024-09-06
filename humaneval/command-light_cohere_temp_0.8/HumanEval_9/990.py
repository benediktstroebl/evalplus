```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:i], numbers[i:]) for i in range(len(numbers)) if i < len(numbers) - 1]
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```