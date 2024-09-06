```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(numbers, reverse=True) if num > numbers[numbers.is_sorted()]]
```
# generate a list of numbers [1,2,3,2,3,4,2,3] and call the function with it
numbers = [1, 2, 3, 2, 3, 4, 2, 3]
result = rolling_max(numbers)
print(result)
```