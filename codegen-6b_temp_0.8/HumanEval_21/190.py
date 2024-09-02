from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    value_range = max(numbers) - min(numbers)
    maximum = 1
    if value_range != 0:
        minimum = 0
        output = [(((x) - minimum) * maximum) / value_range for x in numbers]
    else:
        output = [maximum for x in numbers]
    return output

