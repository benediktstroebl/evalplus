```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    return [max(list(window)) for window in zip_longest(numbers, numbers[1:]+[None])][:-rolling_window]

def zip_longest(*args) -> List[Tuple[object]]:
    return list(zip_longest(*args))
```