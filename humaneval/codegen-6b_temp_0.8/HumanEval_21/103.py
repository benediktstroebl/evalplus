from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = numbers[0]
    max_number = numbers[0]
    for x in numbers:
        if x < min_number:
            min_number = x
        if x > max_number:
            max_number = x

    difference = max_number - min_number
    if difference == 0:
        return numbers

    for i in range(0, len(numbers)):
        numbers[i] = (numbers[i] - min_number) / difference

    return numbers

