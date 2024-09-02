from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    sorted_list = sorted(numbers)
    rescaled_list = [x - sorted_list[0] for x in sorted_list]
    rescaled_list = [x / sorted_list[-1] for x in rescaled_list]
    return rescaled_list
