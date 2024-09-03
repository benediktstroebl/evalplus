from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    number = min(numbers)
    number = max(numbers)
    if number == 0.0:
        return numbers

    # Linear transform a list so that smallest number is 0 and the largest is 1
    numbers = map(lambda num: num/number, numbers)
    return numbers

