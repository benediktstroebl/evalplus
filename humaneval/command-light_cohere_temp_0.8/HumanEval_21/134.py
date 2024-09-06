```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test:
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0.0, 0.0])
    test assert (0.0, 0.0, 0.0) in the in numbers ([0, 4, 0])
    assert rescale_to_unit([0.0, 0]) == [0.0, 0]
assert rescale_to_unit([0.5, 0]) == [0.0, 1.0]
assert rescale_to_unit([0.75, 0]) == [0.0, 0]
```
The function first takes a list of numbers and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It does this by subtracting the smallest number from each number and dividing the result by the sum of all numbers. The result is then multiplied by 1 and then added to the smallest number.