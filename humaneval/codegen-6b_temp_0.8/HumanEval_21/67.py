from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) >= 2
    min_num = min(numbers)
    max_num = max(numbers)
    unit = 1.0 / (max_num - min_num)
    # use map to compute the result since lambda will have problems with mutable types
    return list(map(lambda x: (x - min_num) * unit, numbers))

