from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_num = 0
    list_rolling_max = []
    for number in numbers:
        if number > rolling_max_num:
            rolling_max_num = number
        list_rolling_max.append(rolling_max_num)
    return list_rolling_max

