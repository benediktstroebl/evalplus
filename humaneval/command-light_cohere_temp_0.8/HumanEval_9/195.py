```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, idx in sorted((num, idx) for idx, num in enumerate(numbers)) if idx != numbers.count(max)]
```
Do you require additional help with this code?