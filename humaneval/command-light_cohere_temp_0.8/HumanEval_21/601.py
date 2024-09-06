```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    numbers = [x / 100.0 for x in numbers]
    return numbers
```
The function `rescale_to_unit` takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. The function then returns the result of the linear transformation.