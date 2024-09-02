from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError('This function must be given a list of at least two numbers')

    if all(num == numbers[0] for num in numbers[1:]):
        return [0.0] * len(numbers)

    min_val, max_val = min(numbers), max(numbers)
    return [(num - min_val) / (max_val - min_val) for num in numbers]
