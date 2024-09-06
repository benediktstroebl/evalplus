```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.filter(lambda x: x > numbers[-1])
    return [max(numbers[i-1], x) for i,x in enumerate(numbers)]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```