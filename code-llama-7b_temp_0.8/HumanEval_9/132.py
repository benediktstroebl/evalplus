from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max: int = 0
    rolling_max: List[int] = []
    for num in numbers:
        current_max = max(current_max, num)
        rolling_max.append(current_max)
    return rolling_max

