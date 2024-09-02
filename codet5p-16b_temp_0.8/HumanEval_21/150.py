from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    return [0.0 if numbers[0] > numbers[1] else 1.0 - (numbers[0] / numbers[1])] + \
           [(numbers[i] - numbers[0]) / (numbers[i] - numbers[1]) for i in range(2, len(numbers))]

