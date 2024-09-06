```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in reversed(sorted(numbers)) if x > numbers[-1]]
#Test cases
numbers1 = [1, 2, 3, 4, 5]
print(rolling_max(numbers1))  # [5, 4, 3, 2, 1]
numbers2 = [1, 2, 3, 9, 8, 7]
print(rolling_max(numbers2))  # [9, 8, 7, 6, 5]
numbers3 = [20,)
print(rolling_max(numbers3))  # []
```