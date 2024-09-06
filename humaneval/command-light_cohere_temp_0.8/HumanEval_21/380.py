```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    """
    numbers = [n // (1.0 - 0.0) * n % 1.0 + 0.0)
    last list the this original list
    numbers = [0.0, 0.0, 0.0, 0.0, 1.0]
    original_ numbers = [1.0, 2.0, 3.0, 4.0, 0.0]
    numbers = numbers = numbers
    numbers = [n // (1.0 - 0.0) for n % 1.0 + 0.0]
    home numbers that be numbers, the output is: [0.2, 0.0, 0.0, 0.0, 0.0]