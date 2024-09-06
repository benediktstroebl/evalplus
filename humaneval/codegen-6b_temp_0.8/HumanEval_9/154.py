from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = 0
    for n in numbers:
        if n > max_num:
            max_num = n

    rolling_max_list = [max_num]
    for n in numbers[1:]:
        max_num = max(max_num, n)
        rolling_max_list.append(max_num)

    return rolling_max_list

