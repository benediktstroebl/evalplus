from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError(f"Cannot rescale to unit, expected at least two numbers but got {numbers}")

    min_number = min(numbers)
    max_number = max(numbers)
    scaled_numbers = [(i - min_number) / (max_number - min_number) for i in numbers]
    return scaled_n
