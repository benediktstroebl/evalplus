from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) >= 2, "List must have at least 2 elements"
    minimum = min(numbers)
    maximum = max(numbers)
    scaled = [n - minimum for n in numbers]
    divisor = maximum - minimum
    return [s / divisor for s in scaled]
