from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not numbers:
        raise ValueError('No input numbers provided')
    if len(numbers) == 1:
        return numbers
    min_number = min(numbers)
    max_number = max(numbers)
    if max_number == min_number:
        return [0.0 for _ in numbers]
    return [(i - min_number) / (max_number - min_number) for i in numbers]
