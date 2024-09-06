from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_num: List[int] = []
    cur_max: int = -1
    for number in numbers:
        if number > cur_max:
            cur_max = number
        rolling_max_num.append(cur_max)
    return rolling_max_num

