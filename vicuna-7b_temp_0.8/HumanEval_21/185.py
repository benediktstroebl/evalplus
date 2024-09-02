from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    smallest = numbers[0]
    largest = numbers[-1]
    smallest_diff = smallest - smallest
    largest_diff = largest - largest

    num_scaled = []
    for num in numbers:
        scaled = (num - smallest) / smallest_diff
        num_scaled.append(scaled)
    return num_scaled

