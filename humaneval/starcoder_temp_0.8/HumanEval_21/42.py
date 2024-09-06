from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Make sure we have at least 2 numbers
    if len(numbers) < 2:
        raise ValueError("Need at least two numbers")

    # Sort numbers, get min and max
    numbers.sort()
    min_num = numbers[0]
    max_num = numbers[-1]

    # If min and max are the same, return a list of all 1's
    if min_num == max_num:
        return [1] * len(numbers)

    # Apply linear transform
    return [((n - min_num) / (max_num - min_num)) for n in numbers]
