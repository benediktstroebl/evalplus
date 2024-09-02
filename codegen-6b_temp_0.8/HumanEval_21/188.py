from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    biggest = max(numbers)
    smallest = min(numbers)
    smallest_to_biggest = float(biggest - smallest)
    new_numbers = []
    for number in numbers:
        original_value = number
        new_value = (original_value - smallest) / smallest_to_biggest
        new_numbers.append(new_value)
    return new_numbers

