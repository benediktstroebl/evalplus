```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, i in zip(numbers, numbers[1:]) if i < numbers[0]] + [numbers[0]]
```
Do you want me to help you with any other code problem or help with other technical topics?