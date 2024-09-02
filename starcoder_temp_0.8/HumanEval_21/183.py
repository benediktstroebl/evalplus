from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Fail if there aren't at least two numbers
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to rescale")

    # Compute the original min and max
    orig_min = min(numbers)
    orig_max = max(numbers)

    # Compute the desired min and max
    new_min = 0.0
    new_max = 1.0

    # Compute the linear transform
    linear_transform = (new_max - new_min) / (orig_max - orig_min)

    # Apply the linear transform
    scaled = [linear_transform * (n - orig_min) + new_min for n in numbers]

    return scaled

