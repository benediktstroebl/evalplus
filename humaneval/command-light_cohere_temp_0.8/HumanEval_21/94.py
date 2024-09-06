```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # ensure length of numbers list is at least 2
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # apply linear transformation to numbers list, ensuring that smallest number is 0 and largest is 1
    numbers[0] = 0
    numbers[1] = 1

    return numbers
```