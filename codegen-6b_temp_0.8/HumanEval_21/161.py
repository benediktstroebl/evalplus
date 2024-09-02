from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # min and max are the minimum and maximum values in `numbers`.
    # set is used to efficiently find the proper scale transform.
    # min and max are reassigned at the end of the main loop.
    min, max = min(numbers), max(numbers)
    set_ = set(numbers)
    rescaled = [0.0] * len(numbers)
    for i, value in enumerate(numbers):
        rescaled[i] = rescale_value(value, min, max)
    return rescaled

