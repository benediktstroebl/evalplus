```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort()
    fast=numbers.max()
    max_num=numbers[0]
    while numbers and numbers[0]<max_num:
        numbers.remove(numbers[0])
        numbers.append(numbers[0])
        max_num=numbers[0]
    return numbers
```