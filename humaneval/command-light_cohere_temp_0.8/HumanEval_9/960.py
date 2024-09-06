```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumer())]
```

The function `rolling_max` takes a list of integers and returns a list of the maximum elements found while moving through the sequence from left to right. It uses the important sorting technique, known as `enumer()`, to efficiently compute the maximum element at each moment.