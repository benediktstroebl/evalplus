```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters:
        numbers: list of float, a list of numbers to be scaled.
    return:
        list of float, the scaled numbers with the smallest value becoming 0 and the largest value becoming 1
    """
    numbers = [x / 100.0 for x in numbers]
    return numbers
```