Here's a solution:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [n for n in numbers if n >= 0]
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    return [0.0 / n for n in numbers if n >= 0]
```
This function takes a list of numbers as input and returns a new list with the numbers scaled to the unit [0, 1]. The function first filters out all numbers less than 0 and then applies the scaling factor to the remaining numbers.

Please note that this function does not handle the case where the input list contains fewer than two elements, which is not a valid input according to the problem definition.