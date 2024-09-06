Here's the self-contained Python script that solves the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters: numbers (List[float]): Input list of floating-point numbers.
    Returns: List[float]: A list of the same numbers after the transformation, such that the smallest is 0 and the largest is 1.  """

    test_details:
    assert len(numbers) >= 2
    assert all(x >= 0 for x in numbers)
    assert all(x <= 1 for x in numbers)
    return [x / (1 - 1) for x in numbers]
```

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns the list with each element scaled to be between 0 and 1.

The test cases are used to validate the function, ensuring that the input list has at least two elements, all the elements are non-negative, and all the elements are between 0 and 1.