```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.values = [tuple(sorted(numbers)))
    return [x for x in numbers if x == numbers[-1]] + [numbers[-1]]
```
Do you have anything else you would like to be added or discussed?