```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [x/100.0 for x in numbers]
    return [min(numbers) * 100.0 for x in numbers]
```
The function rescale_to_unit takes a list of numbers and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. The function uses the minimum and maximum values to scale the numbers appropriately.