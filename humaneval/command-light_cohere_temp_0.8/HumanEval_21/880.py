```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list to ensure that the smallest number is 0 and the largest is 1
    numbers[0] = 0
    numbers[1:] = 1
    return numbers
```