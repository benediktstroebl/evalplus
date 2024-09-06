```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Test Cases:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   0.0, 0.0, 0)
   
    >>> rescale_to_unit([0.75, 0.0, 0])
   0.0, 0]
   >>> rescale_to_unit([0.75, 0.0, 0])
   0.0, 0]
    """ Normal Output:
    [0.0, 0.0, 0.0]

Test for length:
    >>> rescale_to_unit([0.75, 0.0, 0])
    out [0.0, 0.0, 0]
   Test for length 3:
    >>> rescale_to_unit([0.75, 0.0, 0])
    out [0.0, 0]

You can use this function to easily transform your Markdown code to the desired format.