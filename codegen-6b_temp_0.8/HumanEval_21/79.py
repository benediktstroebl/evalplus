from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # get the minimum and maximum
    min_num = min(numbers)
    max_num = max(numbers)

    # check which way we have to flip the scale
    if min_num < 0 < max_num:
        return [x * 1 / -1 for x in numbers]
    elif min_num < 0 and max_num > 0:
        return [x * 1 / max_num for x in numbers]
    elif min_num < 0 < max_num:
        return [x * 1 / max_num for x in numbers]
    elif min_num < 0 and max_num < 0:
        return [x * -1 / min_num for x in numbers]
    elif max_num > 0 < min_num:
        return [x * -1 / max_num for x in numbers]
    else:
        return [x / max_num for x in numbers]

