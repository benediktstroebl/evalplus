from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("You must supply a list of at least two elements")
    lowest = min(numbers)
    highest = max(numbers)
    # If the original list contains only one number, or if the list contains only the same number twice,
    # the new list should be [0.0, 1.0] or [1.0, 1.0], respectively
    if lowest == highest:
        return [lowest, highest]

    new_numbers = [(n - lowest) / (highest - lowest) for n in numbers]
    return new_numbers

