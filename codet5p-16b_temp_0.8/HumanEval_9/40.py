from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_list: List[int] = []
    current_max: int = None
    for i, number in enumerate(numbers):
        if i == 0:
            current_max = number
        elif number > current_max:
            current_max = number
        rolling_list.append(current_max)
    return rolling_list

