from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min = 9999999999999
    max = -9999999999999
    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number
    diff = max - min
    result = []
    for number in numbers:
        rescaled = (number - min)/diff
        result.append(rescaled)
    return result

