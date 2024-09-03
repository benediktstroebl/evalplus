from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError(f"Rescale numbers is only defined for lists of at least two elements.")
    # Compute the minimum number, which is 1 and the maximum number which is 10.
    minimum = min(numbers)
    maximum = max(numbers)
    # Get the range of the numbers to rescale into (between 0.0 and 1.0)
    range_min = max(0.0, minimum - 1.0)
    range_max = min(1.0, maximum + 1.0)
    # Apply the linear transformation to the numbers (in the range of [0.0, 1.0]).
    return [number * (range_max - range_min) + range_min for number in numbers]

