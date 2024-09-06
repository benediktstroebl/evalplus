```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    :param numbers: list[float]
    :return: list[float]
    """
    # apply linear transform to numbers list
    numbers_rescale = [x * (1 + y) for x, y in zip(numbers, [0.0, 0.0, 0.0, 0.0]]
    status: [1, 0, 0, 0]
    return numbers_rescale

# test
test_list = [1.0, 2.0, 3.0, 4.0, 0.0]
test_rescale = rescale_to_unit(test_list)

print(test_rescale)

```