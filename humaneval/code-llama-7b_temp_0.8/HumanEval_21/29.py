from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # We can solve this problem using math!
    # To do so, first find the minimum and maximum of the list of numbers
    min_number = min(numbers)
    max_number = max(numbers)
    # Then, we can find the scaling factor using the equation 1/max_number
    scaling_factor = 1 / max_number
    # Finally, we can compute the list of numbers by applying the scaling factor and adding the minimum
    return [number * scaling_factor + min_number for number in numbers]

