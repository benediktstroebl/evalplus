from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    previous_rolling_max = 0
    new_rolling_max = 0
    rolling_max_list = []
    for i in numbers:
        if previous_rolling_max <= i:
            new_rolling_max = i
        else:
            new_rolling_max = previous_rolling_max
        previous_rolling_max = new_rolling_max
        rolling_max_list.append(previous_rolling_max)
    return rolling_max_list

