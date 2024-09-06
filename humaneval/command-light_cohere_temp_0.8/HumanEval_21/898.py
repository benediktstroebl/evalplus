```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    If the list has at least two elements, it will be scaled such that the first number is multiplied by 0.75, and the second number is multiplied by 1.25.
    return [ a dry list of numbers after the transformation.
```