```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, i in zip(numbers, numbers[1:])][-1:]

numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```
Do you have additional questions related to Python programming?