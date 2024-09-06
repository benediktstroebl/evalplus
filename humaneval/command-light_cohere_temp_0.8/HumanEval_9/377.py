```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_values = [x for x in numbers if x == max(numbers)]
    return [max(max_values) for max_values in max_values]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```