from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_maxes = []

    for number in numbers:
        if not rolling_maxes or number > rolling_maxes[-1]:
            rolling_maxes.append(number)
        else:
            rolling_maxes.append(rolling_maxes[-1])

    return rolling_maxes
