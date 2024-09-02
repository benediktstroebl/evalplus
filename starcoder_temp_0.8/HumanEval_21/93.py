from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError(f"Expected a list of at least two numbers, got {numbers}")

    min_number = min(numbers)
    max_number = max(numbers)

    # check if we have a list of just negative numbers
    if min_number < 0 and max_number > 0:
        raise ValueError(f"Expected a list of numbers with no zero-crossing, got {numbers}")

    scale_factor = 1 / (max_number - min_number)
    return [scale_factor * (x - min_number) for x in numbers]
