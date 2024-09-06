from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Find the smallest number in the list
    smallest = min(numbers)

    # Find the largest number in the list
    largest = max(numbers)

    # Compute the difference between the largest and smallest number
    diff = largest - smallest

    # Loop through the list, subtract the smallest number, divide by the difference,
    # and add a small number to avoid dividing by zero
    return [(n - smallest) / (diff + 0.000001) for n in numbers]

