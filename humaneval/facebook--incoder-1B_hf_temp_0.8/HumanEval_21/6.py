from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) == 0:
        return []
    numbers = np.array(numbers)
    scaling_factors = np.max(numbers) / np.max(numbers)
    new_numbers = np.zeros_like(numbers)
    new_numbers[numbers > 0] = numbers / scaling_factors[numbers > 0]
    return new_numbers

