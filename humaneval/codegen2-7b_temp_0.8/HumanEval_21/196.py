from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f'Input must be a list, got {type(numbers)}')
    if len(numbers) < 2:
        raise ValueError('At least two elements are required, got {}'.format(numbers))
    return [min(numbers) / (max(numbers) - min(numbers)), 1.0] if max(numbers)!= min(numbers) else [0.0, 1.0
