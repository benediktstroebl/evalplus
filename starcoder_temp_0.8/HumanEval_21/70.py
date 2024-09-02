from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) == 0:
        raise ValueError("Expected at least one number to rescale")
    max_val = max(numbers)
    min_val = min(numbers)
    if max_val == min_val:
        raise ValueError("Expected list to contain at least two different numbers")
    result = [
        (number - min_val) / (max_val - min_val)
        for number in numbers
    ]
    return result
