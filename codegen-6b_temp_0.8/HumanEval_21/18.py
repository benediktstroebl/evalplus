from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Find the minimum and maximum values
    min_value = min(numbers)
    max_value = max(numbers)
    # find the range
    range_value = max_value - min_value
    # scale each value to the range [0, 1]
    scaled_numbers = []
    for number in numbers:
        scaled_number = (number - min_value) / float(range_value)
        scaled_numbers.append(scaled_number)
    return scaled_numbers

