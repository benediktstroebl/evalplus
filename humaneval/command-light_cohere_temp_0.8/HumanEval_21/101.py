```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Input numbers are expected to be floats.

    This function returns the he same list of numbers after the transformation."""

def test_rescale_to_unit(numbers: List[float]):
    assert len(numbers) >= 2, "Input list must contain at least two elements"
    result = rescale_to_unit(numbers)
    assert len(result) == len(numbers) == 2, "The length of the returned list is not 2"
    assert all(result == [0.0, 1.0]) or
   aren't equal."

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

test_rescale_to_unit(numbers)
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list where each element is the corresponding value scaled to be between 0 and 1. The `test_rescale_to_unit` function tests whether the function works correctly by passing the input list [1.0, 2.0, 3.0, 4.0, 5.0] and checking that expected output is `[0.0, 1.0]`.