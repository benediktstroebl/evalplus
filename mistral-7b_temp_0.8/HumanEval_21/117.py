from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    minimum = min(numbers)
    maximum = max(numbers)
    if minimum == maximum:
        # All numbers are the same, so return a new list with the same number repeated
        return [minimum for _ in numbers]
    return [(number - minimum) / (maximum - minimum) for number in numbers]
