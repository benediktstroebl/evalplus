Here is a self-contained Python script that solves the problem of scaling numbers in a markdown code block:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0.0]
   + 0.0, 0)

    numbers

    # Apply the linear transformation to numbers
    transformed_numbers = [num / (max(numbers) - min(numbers))] * (max(numbers) + min(numbers))

    # Return the transformed numbers
    return transformed_numbers
```