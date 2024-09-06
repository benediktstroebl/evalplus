from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    max_num = max(numbers)
    min_num = min(numbers)
    scale = max_num - min_num
    if max_num == min_num:
        return [1 / len(numbers) for _ in numbers]
    return [(num - min_num) / scale for num in numbers]

