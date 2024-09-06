```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [n for n, idx in sorted((idx for idx, n in enumerate(numbers)) if numbers[idx] > numbers[idx-1])][::-1][2:]
```