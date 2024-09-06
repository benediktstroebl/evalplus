from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    window_max = 0
    rolling_max_list = []
    for n in numbers:
        rolling_max_list.append(max(window_max, n))
        window_max = max(window_max, n)
    return rolling_max_list

