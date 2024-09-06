from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return_list: List[int] = []
    for number in numbers:
        return_list.append(number if len(return_list) == 0 else max(number, return_list[-1]))
    return return_list

