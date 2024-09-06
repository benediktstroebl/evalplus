```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Assertion 1: If the list is empty, the function should raise an AssertionError.
    Assertion 2: If there is only one number in the list, it should return that number unchanged.

    Assertion 2: If the list has two elements, the function should return the ratio of the second element to the first element.

    Example the list has not been tested with more than two elements.

Please note, this is just an example of the problem and you would have to test it with various inputs to ensure the correctness.