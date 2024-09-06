from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Need at least two elements in list")
    min_val, max_val = numbers[0], numbers[0]
    for n in numbers:
        if n > max_val:
            max_val = n
        if n < min_val:
            min_val = n
    return [0.0] + [0.5 * (n - min_val) / (max_val - min_val) for n in numbers
