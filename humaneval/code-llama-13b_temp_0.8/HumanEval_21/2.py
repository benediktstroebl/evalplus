from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_num, max_num = min(numbers), max(numbers)
    # do a check to see if the max and min are the same
    if max_num - min_num != 0:
        return [(x - min_num) / (max_num - min_num) for x in numbers]
    # if the max and min are the same, return a list of 1s
    else:
        return [1] * len(numbers)

