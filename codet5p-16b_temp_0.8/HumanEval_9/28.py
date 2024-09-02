from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max_list: List[int] = []
    rolling_max_list.append(numbers[0])
    for current_number in numbers[1:]:
        rolling_max_list.append(max(current_number, rolling_max_list[-1]))
    return rolling_max_list

