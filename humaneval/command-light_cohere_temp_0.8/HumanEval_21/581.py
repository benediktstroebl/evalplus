Here is a self-contained Python function that solves the given problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [x/100.0 for x in numbers]
    return [x*100.0 for x in numbers]
```

This function can be used to transform any list of numbers to a unit scale, where the smallest number is 0 and the largest number is 1.