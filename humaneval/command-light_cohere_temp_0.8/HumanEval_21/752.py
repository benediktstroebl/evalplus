```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers.sort_values(numbers, key=lambda x: (x, 1.0))
   
    numbers = list(zip(sorted(numbers, key=lambda x: (x, 1.aren the sorted(numbers), reverse=True)))
    return numbers
```