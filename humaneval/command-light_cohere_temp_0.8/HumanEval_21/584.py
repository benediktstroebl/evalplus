```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    :
    input
    list of numbers, returns a list with all values rescaled to the unit of 0.

    Here is an test that the numbers are all positive, and the input list is of at least two elements.
    """