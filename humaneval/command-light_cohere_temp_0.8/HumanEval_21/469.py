```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list to ensure that the smallest value becomes 0 and the largest becomes 1
    numbers = [num / min(numbers) for num, min in zip(numbers)]
    return numbers
```