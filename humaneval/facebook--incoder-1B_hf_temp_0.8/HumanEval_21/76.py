from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if numbers[0] == 0 and numbers[1] == 1:
        return [numbers[0]]
    scale = max(numbers[0] / numbers[1], numbers[1] / numbers[0])
    return [number / scale for number in numbers]

