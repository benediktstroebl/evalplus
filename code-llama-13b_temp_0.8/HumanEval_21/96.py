from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("length of input list must be at least 2")
    numbers_float = list(map(float, numbers))
    min_number = min(numbers_float)
    max_number = max(numbers_float)
    result = [0] * len(numbers)
    for i in range(len(numbers)):
        result[i] = (numbers_float[i] - min_number) / (max_number - min_number)
    return result
