```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    assert len(numbers) >= 2
    numbers = [num / 100 for num in numbers]  # rescale each element to range 0-100
    return numbers
```