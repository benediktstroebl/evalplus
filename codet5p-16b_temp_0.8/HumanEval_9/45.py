from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > rolling_max_list[-1]:
            rolling_max_list.append(numbers[i])
        else:
            rolling_max_list.append(rolling_max_list[-1])
    return rolling_max_list

