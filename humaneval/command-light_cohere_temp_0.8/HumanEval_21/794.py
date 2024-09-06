```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers = [x / 100.0 for x in numbers] + [100.0] * numbers[x[:-1] if len(numbers) < 2 else numbers]
    return numbers
```