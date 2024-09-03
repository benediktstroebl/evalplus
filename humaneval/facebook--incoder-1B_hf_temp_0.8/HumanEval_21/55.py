from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers:
        return numbers
    minimum = numbers[0]
    maximum = numbers[-1]

    # linear interpolation from 0 to 1
    rescaled_values = [number / maximum for number in numbers]
    # linear interpolation from 1 to 0
    rescaled_values[0] = minimum

    return rescaled_values

