from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) == 0:
        return []
    if numbers[0] == 0:
        return numbers[1:]
    factor = min([x / y for x, y in zip(numbers[1:], numbers[:-1])], default=1)
    return [x * factor for x in numbers]

