```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.py_numbers = [1, 2, 3, 2, 3, 4, 2, 3, 4]
    return [x for x in numbers if x == numbers[-1]] + [numbers[-1]]
```