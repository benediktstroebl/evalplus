from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) <= 1:
        raise ValueError("There must be at least 2 elements in numbers")
    result = [0.0] * len(numbers)
    numbers.sort()
    result[0] = numbers[0]
    result[-1] = numbers[-1]
    for i in range(1, len(numbers)-1):
        result[i] = 0.25 * numbers[i] + 0.5 * numbers[i-1] + 0.25 * numbers[i+1]
    return result

