```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    >>>rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   0.0, 0.0, 0
   75, 1.0]

    [in any case: [1.0, 0.0, 3.0, 0.0] will be transformed to [-0.75, 0.75, 3.0, 1.0] where the local numbers, which are all between 0 and 1, are transformed to be within the range [0, 1].
    return

This script defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list where each number has been rescaled so that the smallest value is 0 and the largest value is 1. The test that passes a function to a list of numbers and verifies that the function returns the expected results.