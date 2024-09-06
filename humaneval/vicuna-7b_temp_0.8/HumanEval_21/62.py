from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Find the largest and smallest numbers in the list
    max_val = max(numbers)
    min_val = min(numbers)

    # Scale the numbers so that the smallest number is 0 and the largest number is 1
    return [
        0.0 * x / max_val
        for x in numbers
    ] + [1.0 * x / min_val for x in numbers]

