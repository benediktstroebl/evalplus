from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not isinstance(numbers, list):
        raise ValueError('numbers parameter must be a list of numbers')
    if len(numbers) < 2:
        raise ValueError('numbers parameter must contain at least two numbers')
    if not numbers[0] < numbers[1]:
        raise ValueError('first number in numbers parameter must be less than the second')
    return [x / numbers[-1] for x in numbers]
