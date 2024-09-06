from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    max_val = max(numbers)
    min_val = min(numbers)
    scale_val = (max_val - min_val) / (max_val - numbers[0])
    scaled_numbers = [val * scale_val for val in numbers]
    return scaled_numbers
