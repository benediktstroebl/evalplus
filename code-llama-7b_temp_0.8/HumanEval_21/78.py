from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # find the smallest and largest numbers in the list
    smallest_number = min(numbers)
    largest_number = max(numbers)

    # find the factor to multiply each number by
    factor = 1 / (largest_number - smallest_number)

    # find the constant to add after multiplying by the factor
    constant = -smallest_number * factor

    # multiply each number by the factor and add the constant
    return [number * factor + constant for number in numbers]

