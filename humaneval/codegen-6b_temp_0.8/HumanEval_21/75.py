from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    largest_index = length - 1
    smallest_index = 0
    while largest_index != smallest_index:
        sorted_numbers[smallest_index] = sorted_numbers[smallest_index] / sorted_numbers[largest_index]
        smallest_index += 1
        largest_index -= 1
    return sorted_numbers

