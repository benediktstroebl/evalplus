from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    scale_factors = [1 / (max_number - min_number), 1 / max_number, 1 / min_number]
    scaled_numbers = [min_number + (number - min_number) * factor for number, factor in zip(numbers, scale_factors)]
    return scaled_numbers

