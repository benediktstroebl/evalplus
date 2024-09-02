from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_list: List[int] = []
    for i in range(len(numbers)):
        running_max: int = max(numbers[:i + 1])
        rolling_list.append(running_max)
    return rolling_list

