from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) > 1, "Need more than one number to rescale to unit"
    minimum = min(numbers)
    maximum = max(numbers)
    if maximum > minimum:
        m = maximum - minimum
        if m == 0:
            m = 1
        return [x * 1.0 / m for x in numbers
