from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max = [numbers[0]]
    for current_num in numbers:
        if current_num > rolling_max[-1]:
            rolling_max.append(current_num)
        else:
            rolling_max.append(rolling_max[-1])
    return rolling_max

