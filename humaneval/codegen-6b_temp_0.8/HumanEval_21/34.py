from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # get the min and max values
    lmin = min(numbers)
    lmax = max(numbers)

    # normalize the values
    # we need a final value, so the range is 1.0 - 0.0
    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - lmin) / (lmax - lmin)
    return numbers

