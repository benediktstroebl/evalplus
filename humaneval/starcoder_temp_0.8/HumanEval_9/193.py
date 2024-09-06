from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = max(numbers)
    rolling_maximums: List[int] = [current_max] * len(numbers)
    for i in range(1, len(numbers)):
        rolling_maximums[i] = max(rolling_maximums[i - 1], numbers[i])
    return rolling_maximums

