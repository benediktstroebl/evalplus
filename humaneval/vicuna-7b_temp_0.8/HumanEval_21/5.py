from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    max_value = max(numbers)
    min_value = min(numbers)
    scaled_values = [
        0.0 if value < min_value else
        min_value / max_value * value
        for value in numbers
    ]
    return scaled_values

