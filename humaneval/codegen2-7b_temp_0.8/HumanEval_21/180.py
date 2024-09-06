from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    x = np.sort(numbers)
    if x[0]!= 0:
        x = [0.0] + x
        x = np.cumsum(x)
    else:
        x = x
    return [x[0]] + [(i / x[-1]) for i in x[1:]]

