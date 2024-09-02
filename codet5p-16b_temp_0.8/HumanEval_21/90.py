from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError("Given list must contain at least two numbers!")
    if len(numbers) > 2:
        return [numbers[0]] + [numbers[i] / max(numbers[i+1], numbers[i+2]) for i in range(1, len(numbers) - 1)] + [numbers[-1]]
    else:
        return [numbers[0]] + [numbers[i] / numbers[i + 1] for i in range(len(numbers) - 1)] + [numbers[-1]]
