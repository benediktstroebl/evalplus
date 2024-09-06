```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Define linear transformation
    transform = [1.0, 0.0, 1.0, -0] / numbers[1] + [1.0, 0.0, 0.0]

   
    > numbers[0]
    numbers = [num / transform[idx] for idx, num in enumerate(numbers)]

    return numbers
```