```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    Input: numbers: list of floats, the numbers to be rescaled

    assert len(numbers) >= 2, "Input list must have at least two elements"
    numbers = [x / 100.0 for x in numbers]
    print(numbers)
    return numbers
```