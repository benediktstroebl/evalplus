from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Can't rescale a list with fewer than two elements")

    # Find the minimum and maximum values
    min_val, max_val = min(numbers), max(numbers)

    # If all the numbers are the same, no rescaling is necessary
    if min_val == max_val:
        return numbers

    # Linearly rescale the values so that min_val is 0 and max_val is 1
    return [(val - min_val) / (max_val - min_val) for val in numbers]

