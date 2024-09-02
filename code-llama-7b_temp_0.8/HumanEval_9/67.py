from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []
    for index, number in enumerate(numbers):
        if index == 0:
            rolling_max.append(number)
        else:
            rolling_max.append(max(rolling_max[index - 1], number))
    return rolling_max

