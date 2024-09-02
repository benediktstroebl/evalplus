from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    new_numbers = []
    smallest_number = min(numbers)
    largest_number = max(numbers)
    for number in numbers:
        rescaled_number = (number - smallest_number) / (largest_number - smallest_number)
        new_numbers.append(rescaled_number)
    return new_numbers
