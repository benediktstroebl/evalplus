from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    rounded_numbers = round(numbers)
    # Remove first and last elements as they have already been normalized
    if rounded_numbers[0] > rounded_numbers[-1]:
        rounded_numbers = rounded_numbers[1:]
    # Remove zero values
    if rounded_numbers[0] == 0:
        rounded_numbers = rounded_numbers[1:]
    if rounded_numbers[-1] == 0:
        rounded_numbers = rounded_numbers[:-1]
    unit_rounded = [
        (number - rounded_numbers[0]) / (rounded_numbers[-1] - rounded_numbers[0])
        for number in rounded_numbers
    ]
    return unit_rounded

