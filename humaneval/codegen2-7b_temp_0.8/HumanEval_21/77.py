from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) <= 1:
        return numbers
    sorted_numbers = sorted(numbers)
    unit = 1.0 / (sorted_numbers[-1] - sorted_numbers[0])
    return [0.0 if number == sorted_numbers[0] else unit * (number - sorted_numbers[0]) for number in sorted_numbers
