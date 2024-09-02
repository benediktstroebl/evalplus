from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    n = len(numbers)
    if n < 2:
        return numbers
    scale = numbers[-1] / numbers[0]
    for i in range(n-1):
        scale *= numbers[i+1] - numbers[i]
    return [scale*x for x in numbers]
