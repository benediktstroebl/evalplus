from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # this step ensures there are no floating point rounding errors
    numbers = math.fabs(numbers)
    numbers = [numbers[i] for i in range(0, len(numbers)) if numbers[i] > 0]

    # this is how we would have done it in Python - this is much more elegant
    return [numbers[i] / numbers[0] for i in range(0, len(numbers))]

