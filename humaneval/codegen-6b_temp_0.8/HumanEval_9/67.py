from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max: List[int] = []
    max_number = -1
    for i in numbers:
        max_number = max(i, max_number)
        rolling_max.append(max_number)
    return rolling_max

