from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise ValueError("Need at least two numbers to rescale")
    smallest = numbers[0]
    largest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return [(number - smallest) / (largest - smallest) for number in numbers]

