from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Define the minimum and maximum values
    min_val, max_val = min(numbers), max(numbers)

    # Map the numbers to a range between 0 and 1
    rescaled_numbers = [0.5 * (val - min_val) / (max_val - min_val) + min_val for val in numbers]

    return rescaled_numbers

