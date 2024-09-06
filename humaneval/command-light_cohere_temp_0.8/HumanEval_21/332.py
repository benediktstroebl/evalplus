```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Assertions:
    numbers[-1] == 0  # assertion for validation
    numbers[0]  == 0  # assertion for validation

    return [n / (numbers[-1] - numbers[0])) for n in numbers]
```
This function, "rescale_to_unit," takes a list of numbers and applies a linear transformation to it. It is designed so that the smallest number in the list will become 0, and the largest number will become 1. The function returns the value of the list, which has been rescaled to the unit [0, 1].