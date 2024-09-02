from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) >= 2, "at least two numbers must be provided"
    numbers = sorted(numbers)
    min_value = numbers[0]
    max_value = numbers[-1]
    scale_factor = 1 / (max_value - min_value)
    return [(number - min_value) * scale_factor for number in numbers]

