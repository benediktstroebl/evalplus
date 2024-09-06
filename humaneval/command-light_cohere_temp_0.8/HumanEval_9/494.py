```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.add(numbers[-1], 0)
    max_num = max(numbers)
    rolling_max.add(max_num, 0)
    return [max_num]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```