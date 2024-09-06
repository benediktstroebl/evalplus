from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    scaled_numbers = [0.0 if n < 1.0/10.0 else n for n in numbers]
    for i in range(1, len(scaled_numbers)):
        if scaled_numbers[i] < scaled_numbers[i-1]:
            scaled_numbers[i] = 0.25 * (scaled_numbers[i] - scaled_numbers[i-1])
    return scaled_numbers

