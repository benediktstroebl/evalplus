from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    total = sum(numbers)
    if total == 0:
        return [0.0, 0.0, 1.0]
    min_value = min(numbers)
    max_value = max(numbers)
    scaled_numbers = [x / (max_value - min_value) for x in numbers]
    return [min_value * x + (1 - min_value) * max_value for x in scaled_numbers]

