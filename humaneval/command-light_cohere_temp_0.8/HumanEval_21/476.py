```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Args:
        numbers: list of float (at least 2 elements)

    Returns:
        list of float, with each value scaled to be between 0 and 1
    """
    numbers = [x / max(numbers) for x in numbers] + [max(numbers) / min(numbers)]
    return numbers
```