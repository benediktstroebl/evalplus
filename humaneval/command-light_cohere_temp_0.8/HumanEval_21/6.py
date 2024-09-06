```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 0.5, 0.0]
    to the for numbers are scaled to a unit, where the smallest number is 0 and the largest is 1
    return numbers
```