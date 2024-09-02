from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far: List[int] = []
    max_value: int = None

    for number in numbers:
        max_value = max(max_value or number, number)
        max_so_far.append(max_value)

    return max_so_far

