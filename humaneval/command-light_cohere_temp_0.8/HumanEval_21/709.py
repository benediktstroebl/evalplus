Here is a self-contained Python script that solves the markdown code block problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   75, 1.0]
   
    numbers
    new_scale = [0.0, 0.0, 0.0, 1.0]
    minimum = min(numbers)
    maximum = max(numbers)
    new_scale[0] = numbers[0] / minimum
    new_scale[1] = numbers[1] / maximum
    new_scale[2] = numbers[2] / maximum
    new_scale[3] = numbers[3] / maximum
    return new_scale
```
The function takes a list of numbers as input and returns a new list with the values in the input list rescaled to the range [0, 1].