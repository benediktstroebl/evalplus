from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    pass
    assert len(numbers) >= 2
    numbers.sort()
    min_value = numbers[0]
    max_value = numbers[-1]
    min_numbers = numbers[:2]
    min_numbers.sort()
    min_numbers[0] = 0
    max_numbers = numbers[-2:]
    max_numbers.sort()
    max_numbers[1] = 1
    return min_numbers + max_numbers

