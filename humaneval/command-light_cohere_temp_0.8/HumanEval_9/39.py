```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in sorted(enumerrange(len(numbers)), key=numbers.max)]
```
The function `rolling_max` generates a list of integers in ascending order and returns the list of the maximum elements in the sequence, found using the `max` method of the `numbers` list.