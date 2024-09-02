from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # To solve this problem, you need to know how to calculate a linear function.
    # First, we need the smallest number (minimum) and the largest number (maximum).
    # Subtract the minimum from each number and divide the result by the difference between the maximum and the minimum.
    return [(num - min(numbers)) / (max(numbers) - min(numbers)) for num in numbers]

