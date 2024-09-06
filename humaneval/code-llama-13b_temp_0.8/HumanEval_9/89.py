from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    for number in numbers:
        if not rolling_max_list:
            rolling_max_list.append(number)
        else:
            rolling_max_list.append(max(rolling_max_list[-1], number))

    return rolling_max_list

