from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_found: Tuple[int, int] = (-1, -1)
    max_value: int = -1
    rolling_max: List[int] = []
    for idx, num in enumerate(numbers):
        if num > max_value:
            max_found = (idx, idx)
            max_value = num
        rolling_max.append(max_value)
    return rolling_max

