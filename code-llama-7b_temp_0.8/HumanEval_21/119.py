from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # min_v = min(numbers)
    # max_v = max(numbers)
    # return [((x - min_v) / (max_v - min_v)) for x in numbers]
    min_v = numbers[0]
    max_v = numbers[0]
    for x in numbers:
        if x < min_v:
            min_v = x
        if x > max_v:
            max_v = x
    return [((x - min_v) / (max_v - min_v)) for x in numbers]
