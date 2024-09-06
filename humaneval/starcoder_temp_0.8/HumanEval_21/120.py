from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Copying numbers as the input is mutable
    scaled_numbers = numbers.copy()
    min_number = min(numbers)
    max_number = max(numbers)
    for i, number in enumerate(scaled_numbers):
        scaled_numbers[i] = (number - min_number) / (max_number - min_number)
    return scaled_numbers

