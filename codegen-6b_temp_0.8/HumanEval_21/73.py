from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    result = []
    min_ = min(numbers)
    max_ = max(numbers)
    x_interval = max_ - min_
    if x_interval == 0:
        return numbers
    for number in numbers:
        x = (number - min_) / x_interval
        result.append(x)
    return result


