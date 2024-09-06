```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    : Return the this list of the numbers, after the transformation.  """ Return the numbers, and return a copy of the list with the transformation applied.
```

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5]

rescale_result = rescale_to_unit(numbers)

# The output is expected to be [0.0, 0.0, 0.0, 1.0]