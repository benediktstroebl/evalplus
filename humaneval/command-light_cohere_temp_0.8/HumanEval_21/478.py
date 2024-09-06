```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [x for x in numbers if x >= 0]
    new_numbers = [x * (1 + 1.0 / numbers) for x in numbers if x < 0]
    return new_numbers
```