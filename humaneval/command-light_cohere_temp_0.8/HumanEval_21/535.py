```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0.0, 0])
   
    """ List[float]) -> List[float]
    """
    numbers = [num / min(numbers) for num in numbers]
    return numbers
```