from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    last_max_list = [numbers[0]]
    for n in numbers[1:]:
        last_max_list.append(max(last_max_list[-1], n))
    return last_max_list

