from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    numbers = sorted(numbers)
    smallest, smallest_err = numbers[0], numbers[0]
    for number in numbers[1:]:
        smallest += number - smallest_err
        smallest_err = number
    return [smallest + (x - smallest_err) / (numbers[-1] - smallest_err) for x in numbers]